import random

def new_word():
    """
    Randomly selects a word from words.txt file for each round
    """
    with open('words.txt', 'r') as h:
        words = h.readlines()
    random_word = random.choice(words)[:-1].upper()
    return random_word