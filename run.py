import random
import string                                                                                                                                               

print("Welcome to The HangMan Game")
print("-------------------------------------------")

def play_again():
    answer = input('Would you like to play again? yes/no').lower()
    if answer == 'y' or answer =='yes':
        play_game()
    else:
        pass

def get_word():
    words =["adult","aeroplane","air","aircraft-carrier" ,"airforce" ,"airport" ,"album" ,"alphabet","apple","desk","diamond","dress", "drill","drink","film","finger","fire","milk","store","bottle","out-put","results"]
    return random.choice(words)

    for x in word:
      print("_", end=" ")

def print_hangman(wrong):
  if(wrong == 0):
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 1): 
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 2):
    print("\n+---+")
    print("O   |")
    print("|   |")
    print("    |")
    print("   ===")
  elif(wrong == 3):
    print("\n+---+")
    print(" O  |")
    print("/|  |")
    print("    |")
    print("   ===")
  elif(wrong == 4):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("   ===")
  elif(wrong == 5):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/   |")
    print("   ===")
  elif(wrong == 6):
    print("\n+---+")
    print(" O   |")
    print("/|\  |")
    print("/ \  |")
    print("    ===")


def play_game():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = get_word()
    used_letters = set()
    



        else: 
            lives = lives - 1
            print('your letter,',user_letter,'is not in the list of words')

    if user_letter in used_letters:
       print('You used the same letter before try again')
    else:
      print('the letter is invalid please do try again.') 
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('well done you have guessed the right word', word, '!!')

if __name__ == '__main__':
   play_again()
 
play_game()