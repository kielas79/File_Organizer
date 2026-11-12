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
    "path_folder": current_folder
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

# bad code warning (imma make it better later)
def default_organize(): # Ok so if i want to add settings, this prob won't work for it.
    path = default_settings["path_folder"] # so this function is gonna be default only
    for files in path.iterdir(): # If i do add settings, i'll make it so the
        if files.is_file(): # Dictionary key is the name.
            file_ext = files.suffix.lower()
            if file_ext in default_settings["extensions"]["images"]:
                folder_name = "images"
                folder_dest = path / folder_name
                folder_dest.mkdir(exist_ok=True)
                shutil.move(str(files), str(folder_dest / files.name))
                # umm
                # you know what, i'll just improve it
def improved_organize():
    path = default_settings["path_folder"]
    for files in path.iterdir():
        if files.is_file():
            file_ext = files.suffix.lower() #i'll figure the next part tmrrow
            


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
    
