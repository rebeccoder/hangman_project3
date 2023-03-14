import random
import sys
import os


def clear_terminal():
    """
    Clears the terminal and code sourced from:
    http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf
    """
    os.system("cls" if os.name == "nt" else "clear")


def new_word():
    """
    Randomly selects a word from words.txt file for each round
    """
    with open("words.txt", "r") as h:
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
    title_art()
    print(display_hangman(0))
    print("Type 1: To Play Game")
    print("Type 2: For Instructions")
    print("Type 3: To Exit")

    while True:
        title_page_option = input("Please Choose Option 1,2 or 3 and Press Enter: ")
        if title_page_option == "1":
            play(word)
            break
        elif title_page_option == "2":
            instructions_page()
            continue
        elif title_page_option == "3":
            clear_terminal()
            sys.exit()
            break
        else:
            print("Please Choose Option 1, 2 or 3")
            break


def instructions_page():
    """
    Displays instructions for the user to understand the game
    """
    clear_terminal()
    instructions_art()
    print(
        """
        Start the game by typing 1 and pressing enter on the homepage.
        A hidden word will appear indicating how many letters are in the word.
        Try to guess the word you can only guess one letter at a time.
        Every letter you get wrong will cost you one of your six lives
        and the hanging will commence.
        Once you run out of life the poor man will be hanged!
        Only you can save him by guesing the right word before your lives reach 0.
        GOOD LUCK!
        """
    )

    start = input("Press the enter key to return to the title page.\n")
    title_page()


def play_again():
    """
    This function is called at the end of the game to see
    if the user wants to play again by entering Y or N
    """
    while True:
        play_again_answer = input("Play Again? (Y/N): ")
        if play_again_answer.upper() == "Y":
            clear_terminal()
            word = new_word()
            play(word)
        elif play_again_answer.upper() == "N":
            title_page()
        else:
            continue


def play(word):
    """
    Starts the game, displays the secret word, the picture of the hangman and amount of lives.
    """
    clear_terminal()
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
            print(
                f"You entered {len(guess)} letters.. You can only enter 1 letter at a time!"
            )
        else:
            print(f"{guess} is an invalid answer. Try again.")
        print(display_hangman(lives))
        print(f"Lives left: {lives}\n")
        print("Guess this word: " + " ".join(secret_word) + "\n")
        print("Letters tried: " + ", ".join(guessed_letters) + "\n")
    if end_game:
        clear_terminal()
        dancing_stickman()
        winner_art()
        print(
            f"Congratulaions! You won! You guessed the word {word} and saved that man!"
        )
        play_again()

    else:
        clear_terminal()
        print(display_hangman(0))
        game_over_art()
        print("Uh Oh! You lost! Wouldn't want to be that guy... Better luck next time!")
        print(f"The word you were looking for was: {word}")
        play_again()


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
                """,
    ]
    return stages[lives]


def dancing_stickman():
    print(
        """
                        7_O_/           
                         (/ 
                         /\/' 
                         7   
    """
    )


def title_art():
    # ANSI code for bright green
    print(
        """\033[1;32m 
 
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝ 
 """
    )


def winner_art():
    print(
        """

░██╗░░░░░░░██╗██╗███╗░░██╗███╗░░██╗███████╗██████╗░
░██║░░██╗░░██║██║████╗░██║████╗░██║██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
░░████╔═████║░██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░██║██║░╚███║██║░╚███║███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
    """
    )


def game_over_art():
    print(
        """

░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝                                           
    """
    )


def instructions_art():
    print(
        """
    
█ █▄░█ █▀ ▀█▀ █▀█ █░█ █▀▀ ▀█▀ █ █▀█ █▄░█ █▀
█ █░▀█ ▄█ ░█░ █▀▄ █▄█ █▄▄ ░█░ █ █▄█ █░▀█ ▄█
    """
    )


title_page()
