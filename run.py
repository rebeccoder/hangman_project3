import random

def new_word():
    """
    Randomly selects a word from words.txt file for each round
    """
    with open('words.txt', 'r') as h:
        words = h.readlines()
    random_word = random.choice(words)[:-1].upper()
    return random_word

word = new_word()

def play(word):
    """
    Starts the game, displays the secret word, the picture of the hangman and the amount of lives.
    """

    secret_word = "_" * len(word)
    end_game = False
    guessed_letters = []
    lives = 6
    print("Let's play Hangman!")
    print(display_hangman(lives))
    print("Guess this word: " + " ".join(secret_word) + "\n")
    print("\n")
    """
    Promts for the user to input a letter and returns whether 
    the letter is in the word or not, if it is then it adds the letter
    to the word, if the word is completed then the game is ended
    """
    while not end_game and lives >= 0:
        guess = input("Please try a letter").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You have already tried the letter {guess}!")
            elif guess in word:
                print(f"Uh oh{guess} is not in the word!")
                lives -= 1
                guessed_letters.append(guess)
        else:
            print(f"{guess} is in the word! Well done!")
            guessed_letters.append(guess)
            word_as_list = list(secret_word)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            secret_word = "".join(word_as_list)
            if "_" not in secret_word:
                end_game = True
