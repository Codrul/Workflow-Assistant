import json
from pathlib import Path
import os


CONFIG_PATH = Path("config.json")
def load_config():
    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    except(FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error loading config: {e}')
        return {}


def open_file(file_path):
    path = Path(file_path).expanduser().resolve()
    if not path.exists():
        print(f"[!] Path does not exist: {path}")
        return
    os.startfile(str(path))

def open_by_alias(alias):
    config = load_config()
    path = config.get(alias)
    if path:
        open_file(path)
    else:
        print(f'Alias {alias} not found!')

def launch_selected(event):
    selected = combo.get()
    path = config.get(selected)
    if path:
        open_file(path)