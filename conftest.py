import sys
from pathlib import Path

# Add the project package folder to sys.path explicitly
ROOT = Path(__file__).resolve()
PACKAGE_DIR = ROOT / "library_management_system"

if str(PACKAGE_DIR) not in sys.path:
    sys.path.insert(0, str(PACKAGE_DIR.parent))
