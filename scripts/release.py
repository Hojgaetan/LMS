"""Script d'automatisation de release.

Fonctions principales:
- Détection automatique du type de bump (Conventional Commits) avec --auto
- Bump manuel: --bump major|minor|patch ou --set X.Y.Z
- Mise à jour optionnelle du CHANGELOG (par défaut activée sauf --no-changelog)
- Création du commit et du tag Git correspondants
- Ajout d'un lien de référence en bas du CHANGELOG si remote GitHub détecté

Heuristique Conventional Commits pour --auto :
  - commit contenant "BREAKING CHANGE" ou le préfixe "feat!" / "fix!" -> major
  - commit qui commence par "feat" -> minor
  - commit qui commence par "fix" ou "refactor" ou "perf" -> patch
  - sinon patch si des changements existent

Usage exemples:
  python scripts/release.py --auto
  python scripts/release.py --bump minor
  python scripts/release.py --set 1.0.0
  python scripts/release.py --auto --no-changelog

Pré-requis:
  - Git installé et repo initialisé
  - Fichiers VERSION et CHANGELOG.md présents
"""
from __future__ import annotations
import argparse
import subprocess
import sys
from pathlib import Path
from typing import List, Optional
import re

# Réutilisation des fonctions du script bump_version
try:
    from scripts.bump_version import read_version, write_version, bump, update_changelog  # type: ignore
except Exception as e:  # pragma: no cover
    print(f"Impossible d'importer scripts.bump_version: {e}")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
CHANGELOG_FILE = ROOT / "CHANGELOG.md"
VERSION_FILE = ROOT / "VERSION"

SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)(?:[-+][A-Za-z0-9.]+)?$")


def run(cmd: List[str], check: bool = True, capture: bool = False) -> subprocess.CompletedProcess:
    """Exécute une commande système (wrapper utilitaire)."""
    kwargs = {}
    if capture:
        kwargs.update(dict(stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True))
    result = subprocess.run(cmd, **kwargs)
    if check and result.returncode != 0:
        print(f"Commande échouée: {' '.join(cmd)}")
        if capture:
            print(result.stdout)
            print(result.stderr)
        sys.exit(result.returncode)
    return result


def detect_last_tag() -> Optional[str]:
    try:
        res = run(["git", "tag", "--sort=-v:refname"], capture=True, check=False)
        tags = [t.strip() for t in res.stdout.splitlines() if t.strip()]
        return tags[0] if tags else None
    except Exception:
        return None


def commits_since(tag: Optional[str]) -> List[str]:
    if not tag:
        # Tous les commits (première release) – on peut considérer un patch ou minor
        res = run(["git", "log", "--pretty=%s"], capture=True, check=False)
    else:
        res = run(["git", "log", f"{tag}..HEAD", "--pretty=%s"], capture=True, check=False)
    lines = [l.strip() for l in res.stdout.splitlines() if l.strip()]
    return lines


def infer_bump_type(messages: List[str]) -> str:
    if not messages:
        # Aucun nouveau commit -> pas de release (on lèvera plus tard)
        return "none"
    major_triggers = ("BREAKING CHANGE",)
    for msg in messages:
        lowered = msg.lower()
        if any(k.lower() in lowered for k in major_triggers) or re.match(r"^(feat|fix|refactor|perf)!", lowered):
            return "major"
    for msg in messages:
        if msg.lower().startswith("feat"):
            return "minor"
    for msg in messages:
        if msg.lower().startswith(("fix", "refactor", "perf")):
            return "patch"
    # Par défaut si des changements existent -> patch
    return "patch"


def build_reference_link(previous: Optional[str], new_version: str, remote_url: Optional[str]) -> Optional[str]:
    if not remote_url:
        return None
    # Normaliser remote GitHub style
    # Formats possibles: git@github.com:owner/repo.git ou https://github.com/owner/repo.git
    owner_repo = None
    if remote_url.startswith("git@github.com:"):
        owner_repo = remote_url.split(":", 1)[1]
    elif "github.com" in remote_url:
        parts = remote_url.split("github.com", 1)[1].lstrip("/:")
        owner_repo = parts
    if owner_repo and owner_repo.endswith(".git"):
        owner_repo = owner_repo[:-4]
    if not owner_repo or "/" not in owner_repo:
        return None
    base = f"https://github.com/{owner_repo}"
    if previous:
        return f"[{new_version}]: {base}/compare/v{previous}...v{new_version}"
    else:
        return f"[{new_version}]: {base}/releases/tag/v{new_version}"


def append_reference_link(new_version: str, previous: Optional[str]):
    if not CHANGELOG_FILE.exists():
        return
    try:
        remote = run(["git", "config", "--get", "remote.origin.url"], capture=True, check=False)
        remote_url = remote.stdout.strip() or None
    except Exception:
        remote_url = None
    link = build_reference_link(previous, new_version, remote_url)
    if not link:
        return
    content = CHANGELOG_FILE.read_text(encoding="utf-8")
    if f"[{new_version}]" in content and link in content:
        return  # déjà présent
    # Ajouter à la fin (préserver éventuels liens existants)
    if not content.endswith("\n"):
        content += "\n"
    content += f"{link}\n"
    CHANGELOG_FILE.write_text(content, encoding="utf-8")


def ensure_clean_workspace():
    res = run(["git", "status", "--porcelain"], capture=True, check=False)
    # Autoriser modifications de VERSION / CHANGELOG si on est en mode auto avant commit
    return True if res.returncode == 0 else False


def version_already_tagged(new_version: str) -> bool:
    res = run(["git", "tag", "-l", f"v{new_version}"], capture=True, check=False)
    return f"v{new_version}" in res.stdout.splitlines()


def parse_args():
    p = argparse.ArgumentParser(description="Automatisation de release (SemVer + Conventional Commits)")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--auto", action="store_true", help="Détecter automatiquement le type de bump")
    g.add_argument("--bump", choices=["major", "minor", "patch"], help="Forcer un bump spécifique")
    g.add_argument("--set", dest="set_version", help="Fixer explicitement une version (ex: 1.2.0)")
    p.add_argument("--no-changelog", action="store_true", help="Ne pas insérer de squelette dans CHANGELOG")
    p.add_argument("--dry-run", action="store_true", help="Afficher les actions sans modifier le repo")
    return p.parse_args()


def main():  # pragma: no cover - script d'orchestration
    args = parse_args()

    if not VERSION_FILE.exists():
        print("Fichier VERSION manquant - abandon")
        sys.exit(1)

    previous_tag = detect_last_tag()
    current_version = read_version()

    if args.set_version:
        new_version = args.set_version.strip()
        if not SEMVER_RE.match(new_version):
            print("Format de version invalide (SemVer requis)")
            sys.exit(1)
        bump_type = "explicit"
    elif args.auto:
        messages = commits_since(previous_tag)
        bump_type = infer_bump_type(messages)
        if bump_type == "none":
            print("Aucun nouveau commit depuis le dernier tag -> pas de release")
            sys.exit(0)
        if bump_type == "explicit":  # improbable
            bump_type = "patch"
        new_version = bump(current_version, bump_type) if bump_type in {"major", "minor", "patch"} else current_version
    else:  # --bump fourni
        bump_type = args.bump
        new_version = bump(current_version, bump_type)

    if new_version == current_version and not args.set_version:
        print(f"La version reste {current_version} (aucun bump appliqué)")
        return

    if version_already_tagged(new_version):
        print(f"La version {new_version} est déjà taggée. Abandon pour éviter un doublon.")
        sys.exit(1)

    print(f"Release: {current_version} -> {new_version} (type: {bump_type})")

    if args.dry_run:
        print("--dry-run activé : aucune modification écrite.")
        return

    # Bump + changelog
    write_version(new_version)
    if not args.no_changelog:
        update_changelog(new_version)

    # Ajout du lien de référence
    append_reference_link(new_version, previous_tag[1:] if previous_tag and previous_tag.startswith('v') else previous_tag)

    # Git add/commit/tag
    to_add = ["VERSION"]
    if CHANGELOG_FILE.exists():
        to_add.append("CHANGELOG.md")
    run(["git", "add", *to_add], check=False)
    commit_msg = f"chore(release): v{new_version}"
    run(["git", "commit", "-m", commit_msg], check=False)
    run(["git", "tag", "-a", f"v{new_version}", "-m", f"Release {new_version}"], check=False)

    print("✔️ Release créée localement.")
    print("Prochaines étapes :")
    print("  git push origin main --follow-tags")
    print("  (ou ajuster la branche si nécessaire)")


if __name__ == "__main__":  # pragma: no cover
    main()

