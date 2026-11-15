import os
import json
import shutil
import datetime
import traceback
from pathlib import Path

current_folder = Path(__file__).parent
script_path = Path(__file__).resolve()
print("Current Directory:", current_folder)
default_settings = {
    "extensions": {
        "images": [".jpg", ".jpeg", ".jpe", ".jfif", ".jif", ".png", ".gif", ".wbep", ".avif", ".jxl", ".bmp", ".psd", ".ico", 
                    ".tiff", ".tif", "heic", "heif", ".jxl", 
                    ".svg", ".ai", ".eps", 
                    ".raw", ".cr2", ".nef", ".arw", ".dng", ".orf", ".rw2",
                    ".psd", ".xcf" ],
        "word": [".doc", ".docx", ".odt", ".rtf"],
        "excel": [".xls", ".xlsx", ".csv", ".ods"],
        "pdf": [".pdf"],
        "ppt": [".ppt", ".pptx", ".odp"],
        "exe": [".exe"],
        "videos": [".mkv", "mp4", ".avi", ".mov", ".webm", ".wmv"], 
        },

    "path_folder": current_folder
}

def logs(): # Not finished.gonna make (and learn) it later. 11/11/26
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

def improved_organize(folder_path):
    path = Path(folder_path)
    print(f"Current path: {path}")
    for files in path.iterdir():
        print(files.name)
        print(files.is_file())
        if files.is_file() and files.resolve() != script_path:
            file_ext = files.suffix.lower() #i'll figure the next part tmrrow 11/11/26
            print(file_ext)
            for category, extensions in default_settings["extensions"].items():
                if file_ext in extensions:
                    folder_dest = path / category
                    print(f"moving {files.name} to {folder_dest}")
                    folder_dest.mkdir(exist_ok=True)
                    shutil.move(str(files), str(folder_dest / files.name)) #reminder: add logs
                    break #why does tis not work. fixed


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
                    print("E")
                    try:
                        improved_organize(current_folder)
                    except Exception:
                        traceback.print_exc()
                        input("press enter to close")
                else:
                    print("its 1 OR 2 bro")
        else:
            print("Wrong")