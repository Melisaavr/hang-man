# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Welcome Message
print("Welcome to Hangman!")
print("Let's see if you can guess the word.")

# How to Play
print("\nHow to Play:")
print("1. The computer will choose a secret word.")
print("2. You have to guess one letter at a time.")
print("3. You can only guess letters (no numbers or special characters).")
print("4. You have a limited number of incorrect guesses before you lose the game.")
print("5. Try to guess the word before you run out of guesses!")
print("6. Good luck and have fun!\n")


import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

      