#Project
#Rock paper Scissor
consent = True
while (consent):
    p1=int(input("Player 1:Enter your choice, 1 for Rock, 2 for Paper and 3 for Scissor\n"))
    p2=int(input("Player 2:Enter your choice, 1 for Rock, 2 for Paper and 3 for Scissor\n"))
    if p1 and p2 in [1,2,3]:    
        if(p1==p2):
            print("The Game is a tie")
        elif (p1==1 and p2==2):
            print("Player 2 Wins")
        elif(p1==2 and p2==1):
            print("Player 1 Wins")
        elif (p1==1 and p2==3):
            print("Player 1 Wins")
        elif(p1==3 and p2==1):
            print("Player 2 Wins")
        elif(p1==2 and p2==3):
            print("Player 2 Wins")
        elif(p1==3 and p2==2):
            print("Player 1 Wins")
    else:
        print("Invalid numbers. Please Try Again")
    ask=int(input("Enter do you want to play again? Enter 1 for yes and any other number to stop\n"))

    if ask == 1:
        consent=True
    else:
        consent=False
        print("Game Over. Thank you for playing")

