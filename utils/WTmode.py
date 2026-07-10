from random import randint
import os

word="word"
translation="translation"
description="description"

def spell_mode(WT, times=1):
    for i in range(times):
        os.system("clear")
        question=WT.spelling()
        print("=" * 10)
        print(f"spell the word {question[translation]}")
        print("=" * 10)
        answer=input("answer: ")
        if answer==question[word]:
            print("Correct!")
            input("Press Enter to continue...")
        else:
            print(f"Wrong! The correct answer is {question[word]}.")
            input("Press Enter to continue...")
def multiple_choice_mode1(WT, times=1, choiceamount=4):
    question=WT.multich(choiceamount)
    ramdom_index=randint(0, choiceamount-1)
    question_word=question[ramdom_index]
    for i in range(times):
        os.system("clear")
        print("=" * 10)
        print(f"choose the correct translation for the word {question_word[word]}")
        for i in range(choiceamount):
            print(f"{i+1}. {question[i][translation]}")
        print("=" * 10)
        answer=int(input("answer: "))
        if answer==ramdom_index+1:
            print("Correct!")
            input("Press Enter to continue...")
        else:
            print(f"Wrong! The correct answer is {question_word[translation]}.")
            input("Press Enter to continue...")
def multiple_choice_mode2(WT, times=1, choiceamount=4):
    question=WT.multich(choiceamount)
    ramdom_index=randint(0, choiceamount-1)
    question_word=question[ramdom_index]
    os.system("clear")
    for i in range(times):
        print("=" * 10)
        print(f"choose the correct word for the translation {question_word[translation]}")
        for i in range(choiceamount):
            print(f"{i+1}. {question[i][word]}")
        print("=" * 10)
        answer=int(input("answer: "))
        if answer==ramdom_index+1:
            print("Correct!")
            input("Press Enter to continue...")
        else:
            print(f"Wrong! The correct answer is {question_word[translation]}.")
            input("Press Enter to continue...")


def WTmode(WT):
    while True:
        os.system("clear")
        mode = input("Enter the mode (spell or multiple choice1 or multiple choice2 or quit/exit or help): ")
        if mode == "spell":
            times = input("Enter the number of times you want to spell (default is 1): ")
            spell_mode(WT, times=int(times))
        elif mode == "multiple choice1":
            times = input("Enter the number of times you want to answer multiple choice questions (default is 1): ")
            multiple_choice_mode1(WT, times=int(times))
        elif mode == "quit" or mode == "exit":
            break
        elif mode == "help":
            print("Help: ")
            print("1. spell: Test your spelling skills.")
            print("2. multiple choice1: Answer words questions.")
            print("3. multiple choice2: Answer translation questions.")
            print("4. quit/exit: Leave the program.")
            print("5. help: Show this help message.")
        else:
            print("Invalid mode. Please enter 'spell' or 'multiple choice'.")