#Session 29
#3 Oct 2021
#WORD GUESSING GAME : 

import random
name=input("Enter your name:\n")
words=["hello",'bye','hola','bonjour','bienviendo']
word=random.choice(words)
print("Kindly guess: ")
guesses=""
turns=10
while turns>0:
    failed=0
    for char in word:
      if char in guesses:
        print(char)
      else:
        print("_")
        failed+=1
    if failed==0:
      print("You Win!")
      print("The word is :",word)
      break
    guess=input("Guess the remaining characters :")
    guesses+=guess
    if guess not in word:
      turns-=1
      print("Wrong")
      print("You have" ,turns,"more guesses left!")
      if turns==0:
        print("You loose!")