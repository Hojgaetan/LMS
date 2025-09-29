"""Gestion centralisée de la version de l'application.

La version source est stockée dans le fichier racine VERSION afin de :
- Permettre aux scripts (CI/CD) de la récupérer facilement
- Synchroniser le changelog, les tags Git et l'application
"""
from pathlib import Path

__all__ = ["__version__", "get_version"]


def _read_version_file() -> str:
    version_file = Path(__file__).resolve().parent.parent / "VERSION"
    try:
        return version_file.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return "0.0.0+unknown"


def get_version() -> str:
    """Retourne la version courante (lecture lazy)."""
    return _read_version_file()


# Valeur figée au moment de l'import (utilisable pour affichage rapide)
__version__ = get_version()

