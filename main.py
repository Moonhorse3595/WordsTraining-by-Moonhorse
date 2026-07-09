from packages import *
import os
from glob import glob
files = glob("Words/*.json")
import scripts

word="word"
translation="translation"
description="description"

WE = wordEditing.WordEditor(*files)
if __name__ == "__main__":
    mode = input("Enter mode (WE for Word Editor, WT for Word Trainer):")
    if mode == "WE":
        scripts.WEmode.WEmode(WE)
    elif mode == "WT":
        WT = wordTraining.WordTrainer(WE.content)
        scripts.WTmode.WTmode(WT)
    else:
        print("Invalid mode. Please enter 'WE' or 'WT'.")