#Colour Game
#t=30
#red, blue, green
#enter the correct colour
from  tkinter import *
import random
listColours=["red","blue","yellow","green","purple","orange","black","brown","white"]
score=0
gameTimeLeft=30
def startGame(event):
    if gameTimeLeft==30:
        countdown()
    nextcolour()    
        
def nextcolour():
    global score
    global gameTimeLeft
    if gameTimeLeft>0:
        e.focus_set()
        if e.get().upper()==listColours[1].upper():
            score+=1
        e.delete(0,END)
        random.shuffle(listColours)
        disColours.config(fg=str(listColours[1]),text=str(listColours[0]))
        scoreLab.config(text="Score:"+str(score))
          
def countdown():
    global gameTimeLeft
    if gameTimeLeft > 0:
        gameTimeLeft-=1
    elif gameTimeLeft == 0 :
        thankyou=Label(root,text="Thank You for playing the game.",font="verdana 12 bold")
        thankyou.pack()
        gameTimeLeft = -1
    timeLeftLab.config(text='Time Left'+str(gameTimeLeft))
    timeLeftLab.after(1000,countdown)

root=Tk()
root.title("Colour Game")
root.geometry("550x500")
root.config(bg="gold")

instruc=Label(root,text="Type in the colour of words and not the word text",font="verdana 12 bold")
instruc.pack()

disColours=Label(root,text="",font="verdana 60 bold")
disColours.pack()

scoreLab=Label(root,text="Press enter to start",font="verdana 12 bold")
scoreLab.pack()

timeLeftLab=Label(root,text="Time Left"+str(gameTimeLeft),font="verdana 8 bold")
timeLeftLab.pack()



e=Entry(root)
root.bind("<Return>",startGame)
e.pack()
e.focus_set()


root.mainloop()
