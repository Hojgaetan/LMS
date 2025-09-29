"""Script utilitaire pour gérer la version du projet.

Fonctionnalités :
- Fixer explicitement une version (--set 1.2.3)
- Incrémenter automatiquement (--bump major|minor|patch)
- Préparer une entrée de changelog optionnelle (--update-changelog)

Exemples :
python scripts/bump_version.py --bump patch --update-changelog
python scripts/bump_version.py --set 0.2.0
"""
from __future__ import annotations
import argparse
from pathlib import Path
import re
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = ROOT / "VERSION"
CHANGELOG_FILE = ROOT / "CHANGELOG.md"
SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)(?:[-+][A-Za-z0-9.]+)?$")


def read_version() -> str:
    if VERSION_FILE.exists():
        return VERSION_FILE.read_text(encoding="utf-8").strip()
    return "0.0.0"


def write_version(version: str) -> None:
    VERSION_FILE.write_text(version + "\n", encoding="utf-8")
    print(f"✅ VERSION mis à jour -> {version}")


def bump(version: str, part: str) -> str:
    m = SEMVER_RE.match(version)
    if not m:
        raise ValueError(f"Version actuelle '{version}' invalide (format SemVer attendu)")
    major, minor, patch = map(int, m.groups())
    if part == "major":
        major += 1; minor = 0; patch = 0
    elif part == "minor":
        minor += 1; patch = 0
    elif part == "patch":
        patch += 1
    else:
        raise ValueError("Part doit être major|minor|patch")
    return f"{major}.{minor}.{patch}"


def update_changelog(new_version: str) -> None:
    if not CHANGELOG_FILE.exists():
        print("⚠️ Pas de CHANGELOG.md -> ignoré")
        return
    content = CHANGELOG_FILE.read_text(encoding="utf-8")
    header = f"## [{new_version}] - {date.today()}"  # YYYY-MM-DD
    if header in content:
        print("ℹ️ Entrée changelog déjà présente")
        return
    insertion = f"{header}\n### Ajouté\n- (À compléter)\n\n### Modifié\n- (À compléter)\n\n### Corrigé\n- (À compléter)\n\n"
    # Insère après l'intro (après première ligne '# Changelog')
    lines = content.splitlines()
    try:
        first_header_index = lines.index('# Changelog')
    except ValueError:
        first_header_index = 0
    # Chercher première ligne qui commence par '## [' (première release existante)
    for i, line in enumerate(lines):
        if line.startswith('## ['):
            first_release_index = i
            break
    else:
        first_release_index = len(lines)
    lines.insert(first_release_index, insertion)
    CHANGELOG_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"📝 Changelog mis à jour avec le squelette pour {new_version}")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Utilitaire de mise à jour de version (SemVer)")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument('--set', dest='set_version', help='Fixer une version explicite (ex 1.4.0)')
    g.add_argument('--bump', choices=['major','minor','patch'], help='Incrémenter la version existante')
    p.add_argument('--update-changelog', action='store_true', help='Insérer un bloc de changelog pour la nouvelle version si absent')
    return p.parse_args()


def main():
    args = parse_args()
    current = read_version()
    if args.set_version:
        new_version = args.set_version.strip()
        if not SEMVER_RE.match(new_version):
            raise SystemExit("Erreur: format de version invalide (SemVer requis)")
    else:
        new_version = bump(current, args.bump)
    write_version(new_version)
    if args.update_changelog:
        update_changelog(new_version)
    print("✔️ Terminé. Pensez à : git add VERSION CHANGELOG.md && git commit && git tag -a v{0} -m 'Release {0}'".format(new_version))


if __name__ == '__main__':
    main()

