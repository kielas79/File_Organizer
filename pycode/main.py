import os
import json
import shutil
import datetime
from pathlib import Path

current_folder = os.getcwd()
print("Current Directory:", current_folder)
default_settings = {
    "extensions": {
        "images": [".jpg", ".jpeg", ".jpe", ".jfif", ".jif", ".png", ".gif", ".wbep", ".avif", ".jxl", ".bmp", ".psd", ".ico", 
                    ".tiff", ".tif", "heic", "heif", ".jxl", 
                    ".svg", ".ai", ".eps", 
                    ".raw", ".cr2", ".nef", ".arw", ".dng", ".orf", ".rw2",
                    ".psd", ".xcf" ],
        "documents": {
            "word": [".doc", ".docx", ".odt", ".rtf"],
            "excel": [".xls", ".xlsx", ".csv", ".ods"],
            "pdf": ".pdf",
            "ppt": [".ppt", ".pptx", ".odp"]
        },

    },
    "folder": current_folder
}

def logs():
    os.makedirs("logs", exist_ok=True)
    current_day = datetime.date.today()
    current_day += ".txt"
    with open(current_day, "a"):
        json.load()

def load_settings():
    if not os.path.exists("settings.json"):
        print("Settings not found! applying default settings")
        return default_settings

    with open("settings.json", "r") as i:
        return json.load(i)

def organize():
    hi

print("Maro's File Organizer")   
while True:
    while True:
        print("Options:\n1: Change settings (not working aka nothing done)\n2: Start and target folder")
        option = input("Choose from 1-2. single number. no spaces.\n")
        if option == "1":
            print("still on the works mb")
        elif option == "2":
            print("Do you wish to target a specific folder or use the one where this file is located?")
            while True:
                option = input ("type '1' for choosing a folder. type '2' to use this file's location.")
                if option == "1":
                    print("i might work on this next")
                elif option == "2":
                    print("")
                else:
                    print("its 1 OR 2 bro")
        else:
            print("Wrong")
    
