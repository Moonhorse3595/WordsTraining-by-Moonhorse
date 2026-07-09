import json


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
    def edit_word(self, old_word_id, new_word):
        self.content[id] = new_word
    def delete_word(self, id):
        del self.content[id]
    def add_word(self, word):
        self.content.append(word)
    def find_index(self, word):
        for i, w in enumerate(self.content):
            if w["word"] == word:
                return i
        return -1
    def show_all_words(self):
        for word in self.content:
            print(f"Word: {word['word']}, Translation: {word['translation']}, Description: {word['description']}")
    def save(self, file):
        with open(file, "w", encoding="utf-8") as f:
            json.dump(self.content, f, ensure_ascii=False, indent=4)
