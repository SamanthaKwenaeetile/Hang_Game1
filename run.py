import random
import string

from word import words

def get_valid_word (words):
    word =random.choice(words)
    # this will randomly pick a random word from the list. 
    while '_' in words or ' ' in words:

        return words 

def thehangmangame():
    word = get_valid_word(words)
    word_letters = set(word) 
    # 
    Alphabet = set(string.ascii_lowercase)
    used_letters = set() 
     #  this will keep the words that the user has gussed.

