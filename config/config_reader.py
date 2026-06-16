import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config_json" / "config.json"


def load_config() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def get_section(section_name: str) -> dict:
    config = load_config()
    return config[section_name]


def get_url(endpoint_name: str) -> str:
    config = load_config()

    base_url = config["base_url"].rstrip("/")
    endpoint = config["endpoints"][endpoint_name].lstrip("/")

    return f"{base_url}/{endpoint}"
