import random
import sys
import os

def clear_terminal():
    """
    Clears the terminal and code sourced from:
    http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def new_word():
    """
    Randomly selects a word from words.txt file for each round
    """
    with open('words.txt', 'r') as h:
        words = h.readlines()
    random_word = random.choice(words)[:-1].upper()
    return random_word

word = new_word()

def title_page():
    """ 
    Introduces the player to the game.
    Gives them 3 options, to start the game, read instructions or exit
    """
    clear_terminal()
    print("LET'S PLAY HANGMAN")
    print(display_hangman(0))
    print("Type 1: To play Game")
    print("Type 2: For instructions")
    print("Type 3: To exit")

    while True:
        title_page_option = input("Please choose option 1,2 or 3 and press enter: ")
        if title_page_option == "1":
            play(word)
        elif title_page_option == "2":
            print(instructions)
        elif title_page_option == "3":
            clear_terminal()
            sys.exit()
        else:
            print("Please choose option 1, 2 or 3")

def play(word):
    """
    Starts the game, displays the secret word, the picture of the hangman and amount of lives.
    """
    secret_word = "_" * len(word)
    end_game = False
    guessed_letters = []
    lives = 6
    print("Let's play Hangman!")
    print(display_hangman(lives))
    print(f"Lives: {lives}\n")
    print("Guess this word: " + " ".join(secret_word) + "\n")
    print("\n")
    """
    Promts for the user to input a letter and returns whether 
    the letter is in the word or not, if it is then it adds the letter
    to the word, if the word is completed then the winning/losing message is shown
    """
    while not end_game and lives > 0:
        guess = input("Please type a letter and then press enter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You have already tried the letter {guess}!")
            elif guess in word:
                print(f"{guess} is in the word! Well done!")
                guessed_letters.append(guess)
                word_as_list = list(secret_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                secret_word = "".join(word_as_list)
                if "_" not in secret_word:
                    end_game = True
            else:
                print(f"Uh oh {guess} is not in the word!")
                lives -= 1
                guessed_letters.append(guess)

        elif len(guess) != 1:
            print(f"You entered {len(guess)} letters.. You can only enter 1 letter at a time!")
        else:
            print(f"{guess} is an invalid answer. Try again.")
        print(display_hangman(lives))
        print(f"Lives left: {lives}\n")
        print("Guess this word: " + " ".join(secret_word) + "\n")
        print("Letters tried: " + ", ".join(guessed_letters) + "\n")
    if end_game:
        print("Congratulaions! You guessed the word, you've won!")
        while input("Play Again? (Y/N) ").upper() == "Y":
            if True:
                clear_terminal()
                word = new_word()
                play(word)
            else:
                title_page()
    else:
        print("Sorry you've ran out of lives. Better luck next time!")
        print(f"The word you were looking for was: {word}")
        while input("Play Again? (Y/N) ").upper() == "Y":
            if True:
                clear_terminal()
                word = new_word()
                play(word)
            else:
                title_page()

    

def display_hangman(lives):
    """
    Copied and pasted from youtube code credited in the README
    Displays the hangman lives visual representation for the user
    """
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[lives]


title_page()
"""
def main():
    title_page()
    word = new_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        if True:
            word = new_word()
            play(word)
        else:
            title_page()

main()
"""