# HANGMAN

## Introduction

For my 3rd Portfolio Project for the Code Institute I have chosen to make a classic Hangman game.
It's a Python terminal game that runs through the Code Institute terminal on Heroku.

Users will be greated with a Title page which will provide 3 options - to play the game, read instructions or to end the game. 
It is a single player game designed to be simple to use yet challenging.

## How to play

Hangman is originally a game drawn on a peice of paper with 2 or more players with 1 of the players choosing the word in question and drawing the hangman when the letters are guessed wrong. In this version, however, the computer programme is the player picking the word and drawing the hangman while the user is trying to guess what that word is. 
The instructions can be found for this page on option 2 of the title page.
When the user chooses to start the game a word to be guessed is randomly chosen from a list of words stored in the programme and will be displayed as "_ _ _ _ _ _" along with the amount of lives they have.
The user is also prompted to enter a letter. If they guess it right the letter is added to the hidden word wherever it is supposed to be, for example "_ _ e _ _ d _ e" until the word is complete. If they guess any letters wrong then any lives will automatically be deducted and an image of a hangmam at different stages depending on the number of incorrect guesses.
This process continues until either the user guesses the word correct before running out of lives and the winning screen 
appears or being directed the losing screen if they run out of lives before they guess the word.

## User Experience(UX)
### Stratergy

#### Target Audience
      - All ages
      - All levels
      - English Speakers

#### User Goals.
      - As a User, I want to easily navigate through the game with simple inputs
      - As a User, I want to understand how to play they game
      - As a User, I want to have fun and enjoy the game

#### Objectives
      - Provide a fully functions and smooth running game
      - Make the game fun, quick, yet challenging
      - Ensure the game is easy and intuitive to use

### Scope

Based on objectives and user stories.

#### Requirements
     - Give clear and digestable instructions
     - Allow the game to run through without needing to refresh or leave the page
     - Ensure there's a new word with every new game

### Structure

The game is ran through a python terminal on a webpage. It's deployed using Heroku which is connected to GitHub.
The user only needs to enter single characters followed by the Enter key.

### Skeleton

Here is a logic flow chart I made for the hangman game.
I created this to have a visual plan of the game cycle.
I wanted to make sure that I was creating a game that you didn't have to leave the terminal to keep playing as many rounds as you want to play. The user shouldn't even have to move their mouse as everything has been programmed into the keys. This chart shows how this programme should keep flowing.