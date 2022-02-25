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
    lives = lives - 1 
    print('your letter,' , user_letter, 'is nit in the list of words')

if user_letter in used_letters:
        print('You used the same letter before try again')
    
else:
    print('the letter that has been enterd is invalid please do try again.')


 
# gets here when len(word_letters) == 0 OR when lives == 0
if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)

else:
    print('well done you have guessed the right word', word, '!!')
   
        
if __name__ == '__main__':
    thehangmangame()

