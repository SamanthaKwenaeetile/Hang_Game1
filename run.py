import random
import string

from word import word

def get_valid_word (word):
    word =random.choice(word)
    # this will randomly pick a random word from the list. 
    while '_' in word or ' ' in word:

        return word.lower()

def thehangmangame():
    word = get_valid_word(word)
    word_letters = set(word) 
    # 
    Alphabet = set(string.ascii_lowercase)
    used_letters = set() 
     #  this will keep the words that the user has gussed.

# the user input 
while len(word_letters) >0:
    # the letters that the users have used
    print('these letters you have used', ''.join(used_letters))

 # 
user_letter = input('Guess a letter:').ascii_lowercase()
if user_letter in Alphabet - used_letters:
    used_letters.add(used_letter)
    if used_letter in word_letters:
        word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print('You used the same letter before try again')
    
    else:
        print('invalid letter enterd please try again')
        




