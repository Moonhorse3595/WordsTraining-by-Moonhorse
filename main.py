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
    mode = input("Enter mode (WE for Word Editor, WT for Word Trainer):")
    if mode == "WE":
        utils.WEmode.WEmode(WE)
    elif mode == "WT":
        WT = wordTraining.WordTrainer(WE.content)
        utils.WTmode.WTmode(WT)
    else:
        print("Invalid mode. Please enter 'WE' or 'WT'.")