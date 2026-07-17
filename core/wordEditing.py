import json
import os

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

class WordEditor():
    def __init__(self, *files):
        for file in files:
            try:
                with open(file, "r", encoding="utf-8") as f:
                    self.content = json.load(f)
                    self.content=list(self.content)
            except FileNotFoundError:
                print(f"File {file} not found.")
                self.content = ""
    def edit_word(self, old_word, new_word):
        self.content[self.find_index(old_word)] = new_word
    def delete_word(self, id):
        del self.content[id]
    def add_word(self, word):
        self.content.append(word)
    def find_index(self, word):
        for i, w in enumerate(self.content):
            if w["word"] == word:
                return int(i)
        return -1
    def show_all_words(self):
        for word in self.content:
            print(f"Word: {word['word']}, Translation: {word['translation']}, Description: {word['description']}")
    def save_file(self, file):
        with open(file, "w", encoding="utf-8") as f:
            json.dump(self.content, f, ensure_ascii=False, indent=4)
    def load_files(self, *files):
        for file in files:
            try:
                with open(file, "r", encoding="utf-8") as f:
                    new_content = json.load(f)
                    self.content.extend(new_content)
            except FileNotFoundError:
                print(f"File {file} not found.")
