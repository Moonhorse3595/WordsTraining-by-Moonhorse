# WordsTraining-by-Moonhorse
To Train words and translation
## wordEditing.py
- class WordEditor(*files):
    - edit_word(old_word, new_word)
    - delete_word(id)
    - add_word(word)
    - find_index(word)
    - show_all_words()
    - save_file(file)
```python
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
```
## wordTraining.py
- class WordTrainer(words):   <span style="color: green"># WordEditor.content</span>
    - multich
        - return choices
    - spell
        - return a word

```python
import random

class WordTrainer():
    def __init__(self, words):
        self.words=words
    def multich(self, choiceamount):
        if choiceamount>len(self.words):
            raise ValueError("choiceamount cannot be greater than the number of words.")
        choices=random.sample(self.words, choiceamount)
        return choices
    def spelling(self):
        if not self.words:
            raise ValueError("No words available for spelling.")
        else:
            word=random.choice(self.words)
            return word

```