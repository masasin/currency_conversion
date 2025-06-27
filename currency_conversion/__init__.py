import tomllib
from pathlib import Path

with open(Path(__file__).parent.parent / "pyproject.toml", "rb") as f:
    data = tomllib.load(f)

DATA_DIR = Path(f"~/.local/share/{data['project']['name']}").expanduser()
