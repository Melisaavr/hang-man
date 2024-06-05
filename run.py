import random
from words import words  # Assuming words.py contains a list of words
from hangman_visual import lives_visual_dict  # Assuming hangman_visual.py contains visual representations for lives
import string
import time

def print_rules():
    """
    Print the welcome message and game rules.
    """
    print(f"""
Welcome to Hangman!
Let's see if you can guess the word.

How to Play
1. The computer will choose a secret word.
2. You have to guess one letter at a time.
3. You can only guess letters (no numbers or special characters).
4. You have a limited number of incorrect guesses before you lose the game.
5. Try to guess the word before you run out of guesses!
6. Good luck and have fun!
""")

def get_valid_word(words):
    """
    Randomly choose a valid word from the list.

    Args:
        words (list): List of potential words to choose from.

    Returns:
        str: A valid word in uppercase letters.
    """
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def display_game_state(used_letters, lives, word_list, start_time):
    """
    Display the current state of the game.

    Args:
        used_letters (set): The set of letters that have been guessed.
        lives (int): The number of lives remaining.
        word_list (list): The current state of the word being guessed.
        start_time (float): The start time of the game.
    """
    print(f'You have {lives} lives left and you have used these letters: {" ".join(used_letters)}')
    elapsed_time = int(time.time() - start_time)
    print(f'Time elapsed: {elapsed_time} seconds')
    print(lives_visual_dict[lives])
    print(f'Current word: {" ".join(word_list)}')

def hangman():
    """
    Main function to play the Hangman game.
    """
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7
    start_time = time.time()

    while len(word_letters) > 0 and lives > 0:
        display_game_state(used_letters, lives, [letter if letter in used_letters else '-' for letter in word], start_time)
        user_letter = input('Guess a letter: ').upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives -= 1
                print(f'\nYour letter, {user_letter}, is not in the word.')
        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another.')
        else:
            print('\nThat is not a valid letter.')

    if lives == 0:
        print(lives_visual_dict[lives])
        print(f'You died, sorry. The word was {word}')
    else:
        print(f'YAY! You guessed the word {word}!!')

def play_again():
    """
    Ask the player if they want to play again.

    Returns:
        bool: True if the player wants to play again, False otherwise.
    """
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice in ['yes', 'no']:
            return choice == 'yes'
        else:
            print("Invalid input. Please try again.")

def main():
    """
    Main function to run the Hangman game.
    """
    print_rules()
    while True:
        hangman()
        if not play_again():
            print("Thank you for playing. See you next time!")
            break

if __name__ == '__main__':
    main()
