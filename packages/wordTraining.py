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