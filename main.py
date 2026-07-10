from core import *
import os
from glob import glob
files = glob("words/*.json")
import utils

word="word"
translation="translation"
description="description"

WE = wordEditing.WordEditor(*files)
if __name__ == "__main__":
    while True:
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
        elif mode == "quit" or mode == "exit":
            break
        else:
            print("Invalid mode. Please enter 'WE' or 'WT'.")