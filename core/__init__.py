import os
import sys

import core.wordEditing as wordEditing
import core.wordTraining as wordTraining


def clear_screen():
    if sys.platform == "win32":
        os.system("cls")
    elif sys.platform == "darwin":
        os.system("clear")
    elif sys.platform.startswith("linux"):
        os.system("clear")
