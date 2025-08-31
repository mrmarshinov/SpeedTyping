import json
import os

default_settings ={
        "windows_size": "1280x720",
        "difficulty": "Easy",
        "language": "English"
    }
SETTING_FILE = "settings.json"

def load_settings():
    if os.path.exists(SETTING_FILE):
        with open("settings.json", "r", encoding="utf-8") as file_settings:
            return json.load(file_settings)
    else:
        return default_settings

def save_settings(settings):
    with open("settings.json", "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4,ensure_ascii=False)
