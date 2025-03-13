import random as rn 
import string as str
def isWordNotGuessed(list):
  return False in list
def init_users_guess(word_chosen):
  new_list = [] 
  for i in range(len(word_chosen)):
    if word_chosen[i] in str.punctuation or word_chosen[i] == " ":
      new_list.append(True)
    else:
      new_list.append(False)
  return new_list
def start_dialog():
  print("welcome to the Hangman game!")
  print("your goal is to guess the name of the song, you got 6 mistakes in total")
  print("GLHF")
def print_stage(user_guess,word_chosen,life):
  for i in range(len(user_guess)):
    if user_guess[i]:
      print(word_chosen[i],end="")
    else:
      print("_",end="")
  print(f"\nlifes {life}/6")
 


word_list = [ "In the End",    "Hey Ya!",    "Hips Don't Lie",    "Seven Nation Army",    "Toxic",    "Mr. Brightside",    "Crazy in Love",    "Clocks",    "Hot in Herre",    "Umbrella",    "I Gotta Feeling",    "Rolling in the Deep",    "Lose Yourself"]
word_chosen =  rn.choice(word_list)

user_guess = init_users_guess(word_chosen) 
users_lifes = 6 

start_dialog()

while isWordNotGuessed(user_guess) and users_lifes != 0:
  print_stage(user_guess,word_chosen,users_lifes)
  guess = input("\nplease choose a lettes a-z (please make sure to input lowercase letter)\n")
  if guess not in str.ascii_lowercase:
    break
  else:
    if guess in word_chosen.lower():
      for i in range(len(word_chosen)):
        if guess == word_chosen[i].lower():
          user_guess[i] = True
    else: 
      users_lifes-=1
      
    

if not isWordNotGuessed(user_guess):
  print('Congratz! you WON the game!!')
else:
  print('sorry.. you LOST the game')
 