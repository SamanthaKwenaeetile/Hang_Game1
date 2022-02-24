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
    Alphabet = set(string.ascii_lowercase)
    used_letters = set() 
     #  this will keep the words that the user has gussed.

lives = 5

# the user input 
while len(word_letters) >0:
    # the letters that the users have used
    print('these letters you have used', ''.join(used_letters))



# current word 

word_list = [letter if letter in used_letters else '-' for letter in word]
print(lives_dict[lives])
print('the current word is : ', ' '.join(word_list))

user_letter = input('Guess a letter:').ascii_lowercase()
if user_letter in Alphabet - used_letters:
    used_letters.add(used_letter)
    if used_letter in word_letters:
        word_letters.remove(user_letter)
        print('')

 else: 
        lives = lives - 1  # to take away a life if wrong word
         print('\nYour letter,', user_letter, 'is not in the word.')

    elif user_letter in used_letters:
        print('You used the same letter before try again')
    
    else:
        print('invalid letter enterd please try again')


 # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    thehangmangame()


