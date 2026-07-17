import os

from core import clear_screen
from core.wordEditing import load_files
from core.wordEditing import WordEditor

def keepInput(msg):
    while True:
        user_input = input(msg)
        if user_input.strip() == "":
            print("Input cannot be empty. Please try again.")
        else:
            return user_input


def WEmode(WE):
    while True:
        clear_screen()
        print("Word Editor Mode")
        print("1. Edit Word")
        print("2. Delete Word")
        print("3. Add Word")
        print("4. Save File")
        print("5. Show All Words")
        print("6. Load Other File")
        print("7. Help")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            old_word = keepInput("Enter the word to edit: ")
            if WE.find_index(old_word) == -1:
                print(f"Word '{old_word}' not found.")
                input("Press Enter to continue...")
                continue
            else:
                pass
            new_word_word = input("Enter the new word: ")
            new_word_translation = input("Enter the new translation: ")
            new_word_description = input("Enter the new description: ")
            new_word = {
                "word": new_word_word,
                "translation": new_word_translation,
                "description": new_word_description,
            }
            WE.edit_word(old_word, new_word)
        elif choice == "2":
            file_index = WE.find_index(input("Enter the word to delete: "))
            if file_index == -1:
                print("Word not found.")
                input("Press Enter to continue...")
                continue
            WE.delete_word(file_index)
        elif choice == "3":
            new_word_word = keepInput("Enter the new word: ")
            new_word_translation = keepInput("Enter the new translation: ")
            new_word_description = keepInput("Enter the new description: ")
            new_word = {
                "word": new_word_word,
                "translation": new_word_translation,
                "description": new_word_description,
            }
            WE.add_word(new_word)
        elif choice == "4":
            folder = keepInput(
                "Enter the folder name to save the file (default: Words): "
            )
            if not folder:
                folder = "Words"
            if not os.path.exists(folder):
                os.makedirs(folder)
            fileName = keepInput(
                "Enter the file name to save the file (default: words.json): "
            )
            if not fileName:
                fileName = "words.json"
            filePath = os.path.join(folder, fileName)
            WE.save_file(filePath)
        elif choice == "5":
            try:
                WE.show_all_words()
                input("Press Enter to continue...")
            except Exception as e:
                print(f"An error occurred: {e}")
                input("Press Enter to continue...")
        elif choice == "6":
            files = load_files()
            WE.load_files(*files)
        elif choice == "7":
            print("Help: ")
            print("1. Edit Word: Edit an existing word in the list.")
            print("2. Delete Word: Delete a word from the list.")
            print("3. Add Word: Add a new word to the list.")
            print("4. Save File: Save the current list of words to a file.")
            print("5. Show All Words: Display all words in the list.")
            print("6. Load Other File: Load another JSON file.")
            print("7. Help: Show this help message.")
            print("8. Exit: Exit the Word Editor Mode.")
            input("Press Enter to continue...")
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")
