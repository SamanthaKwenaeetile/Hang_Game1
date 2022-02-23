import random
import string

from word import word

def get_valid_word (word):
    word =random.choice(word)
    # this will randomly pick a random word from the list. 
    while '_' in word or ' ' in word:

        return word

def thehangmangame():
    word = get_valid_word(word)
    word_letters = set(word) 
    # 
    Alphabet = set(string.ascii_lowercase)
    used_letters = set() 
     #  this will keep the words that the user has gussed.

# the user input 
user_letter = input('Guess a letter:').ascii_lowercase()
if user_letter in Alphabet - used_letters:
    used_letters.add(used_letter)
    if used_letter in word_letters:
        word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print('You used the same letter before try again')
    
    else:
        print('invalid letter enterd please try again')
        
user_input = input ('enter a letter here')
print(user_input)

