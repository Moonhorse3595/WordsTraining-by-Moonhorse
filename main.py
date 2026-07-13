import os
from glob import glob

from core import *

files = glob("data/*.json")
import utils

word = "word"
translation = "translation"
description = "description"

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
