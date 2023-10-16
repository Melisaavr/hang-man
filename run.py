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

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to display the word with guessed letters
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display