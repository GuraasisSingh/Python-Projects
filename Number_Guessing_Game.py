#Making a number guessing game
import random
up=int(input("Enter the Upper Limit:\n"))
lo=int(input("Enter the Lower Limit:\n"))
n=random.randint(lo,up)
chance=int((up-lo)/4)
if chance==0:
    chance=1

while(True):
    print("You have",chance,"chances to guess the number.")
    
    g=int(input("Guess the number:\n"))
    chance-=1
    if g==n:
        print("Congratulations, You Guessed the number!")
        break
    elif g>n:
        print("The number entered is greater. A smaller number is required.")
    else:
        print("The number entered is smaller. A greater number is required.")
    if chance==0:
        print("You failed to guess the number.")
        print("The number is",n)
        break
