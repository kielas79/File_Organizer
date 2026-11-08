import os
import json
import shutil
import datetime
print("Maro's File Organizer")

default_settings = {
    "extensions": {
        "Documents": [""],
        "Images": [""],

    }
}

def logs():
    os.makedirs("logs", exist_ok=True)
    current_day = datetime.date.today()
    current_day += ".txt"
    with open(current_day, "a"):
        json.load()

def load_settings():
    if not os.path.exists("settings.json"):
        with open("settings.json", "w") as i:
            json.dump(default_settings, i)
            return default_settings

    with open("settings.json", "r") as i:
        return json.load(i)
    
while True:
    print("")
    
