import random
from words import words
from hangman_visual import lives_visual_dict
import string
import time


""" Welcome Message """
def print_rules():
    print(
f""""
Welcome to Hangman!
Let's see if you can guess the word.

How to Play
1. The computer will choose a secret word.
2. You have to guess one letter at a time.
3. You can only guess letters (no numbers or special characters).
4. You have a limited number of incorrect guesses before you lose the game.
5. Try to guess the word before you run out of guesses!
6. Good luck and have fun!
""" )


def menu():
    input("Press enter to start the game")
    hangman()

  
def get_valid_word(words):
    """ randomly chooses something from the list """
    word = random.choice(words)  
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    """ letters in the word """
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  

    lives = 7
    """ Add a timer, starting from the beginning of the game """
    start_time = time.time()  
    

    """ getting user input """
    while len(word_letters) > 0 and lives > 0:
        """letters used """
        """ ' '.join(['a', 'b', 'cd']) --> 'a b cd' """
        print('You have', lives, 
              'lives left and you have used these letters: '
              , ' '.join(used_letters))

    
        elapsed_time = int(time.time() - start_time)
        print(f'Time elapsed: {elapsed_time} seconds')
        

        word_list = [letter if letter in used_letters 
                     else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another.')

        else:
            print('\nThat is not a valid letter.')
            

    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


def play_again():
    choice = input("Do you want to play again? (yes/no): ").lower()
    return choice == 'yes'

def main():
    print_rules()
    while True:
        hangman()
        if not play_again():
            break

if __name__ == '__main__':
    main()

