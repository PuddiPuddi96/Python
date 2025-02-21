import json
from random import choice

class DataManager():

    def __init__(self):
        self.words = self.__load_words()
    
    def __load_words(self):
        data = None
        with open(file="./data.json", mode="r") as file:
            data = json.load(file)
        return data["data"]

    def get_random_word(self):
        return choice(self.words)
