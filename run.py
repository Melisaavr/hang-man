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
import time


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
    start_time = time.time()  # Add a timer, starting from the beginning of the game
    

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

     # Check the timer
        elapsed_time = int(time.time() - start_time)
        print(f'Time elapsed: {elapsed_time} seconds')
        

       # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')
            
# gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


def main():
    hangman()
if __name__ == '__main__':
    main()
