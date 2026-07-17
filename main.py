import os
# from glob import glob

from core import *

# files = glob("data/*.json")
def load_files():
    files=[]
    while True:
        file_path = input("Enter the path to a JSON file (or type 'done' to finish): ")
        if file_path.lower() == 'done':
            break
        elif os.path.isfile(file_path) and file_path.endswith('.json'):
            files.append(file_path)
        else:
            print("Invalid file path. Please enter a valid JSON file path.")
    return files
import utils

word = "word"
translation = "translation"
description = "description"

files = load_files()
WE = wordEditing.WordEditor(*files)
if __name__ == "__main__":
    while True:
        clear_screen()
        mode = input("Enter mode (WE for Word Editor, WT for Word Trainer):")
        if mode == "WE":
            utils.WEmode.WEmode(WE)
        elif mode == "WT":
            WT = wordTraining.WordTrainer(WE.content)
            utils.WTmode.WTmode(WT)
        elif mode == "help":
            print("Available modes:")
            print("WE - Word Editor")
            print("WT - Word Trainer")
            print("quit or exit - Exit the program")
            input("Press Enter to continue...")
        elif mode == "quit" or mode == "exit":
            break
        else:
            print("Invalid mode. Please enter 'WE' or 'WT'.")
            input("Press Enter to continue...")
