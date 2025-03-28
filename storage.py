import json
import os

FILE_PATH = "data/library.json"

def load_library():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    return []

def save_library(books):
    with open(FILE_PATH, "w") as file:
        json.dump(books, file, indent=4)
