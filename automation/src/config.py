import json
from pathlib import Path

DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "config" / "settings.json"

def load_settings(path: str | None = None) -> dict:
    """
    Loads settings from automation/config/settings.json.
    User should copy settings.example.json -> settings.json locally.
    """
    cfg_path = Path(path) if path else DEFAULT_CONFIG_PATH
    if not cfg_path.exists():
        raise FileNotFoundError(
            f"Config not found: {cfg_path}\n"
            f"Create it by copying settings.example.json to settings.json"
        )
    return json.loads(cfg_path.read_text(encoding="utf-8"))
