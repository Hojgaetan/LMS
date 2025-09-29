import re
from core.version import __version__, get_version

SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][A-Za-z0-9.]+)?$")

def test_version_consistency():
    assert __version__ == get_version(), "__version__ et get_version() doivent retourner la même valeur"


def test_version_format():
    assert SEMVER_RE.match(__version__), f"La version '{__version__}' ne respecte pas le format SemVer"

