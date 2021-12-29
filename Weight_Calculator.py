#Session 43
#1 kg *2.20462= pounds
#1 kg * 35.274 = ounce
#1kg *1000 =grams

from tkinter import *
root=Tk()
root.title("Weight Calculator")
root.geometry("500x500")
root.config(bg="green3")

def calculation():
    w=int(kgweight.get())
    gramweight= w*1000
    poundweight= w*2.20462
    ounceweight=w*35.274
    gram=Label(text=f"Your weight in grams is {gramweight}",font="verdana 10 bold", bg ="yellow",fg="blue")
    gram.place(x=120,y=220)
    pound=Label(text=f"Your weight in pounds is {poundweight}",font="verdana 10 bold", bg ="yellow",fg="blue")
    pound.place(x=120,y=270)
    ounce=Label(text=f"Your weight in ounces is {ounceweight}",font="verdana 10 bold", bg ="yellow",fg="blue")
    ounce.place(x=120,y=320)

def clear():
    kgweight.delete(0,END)

def exit():
    root.destroy()

WtEn=Label(root,text="Enter your weight:",font="verdana 10 bold", bg ="yellow",fg="blue")
WtEn.place(x=40, y=40)

wv=StringVar()
kgweight=Entry(root,font="verdana 10 bold",textvar=wv, width=8, bg="white", fg="black")
kgweight.place(x=230,y=40)

cal=Button(root,text="Calculate",font="verdana 10 bold", bg ="yellow",fg="blue",command=calculation)
cal.place(x=40,y=130)

Exit=Button(root,text="Exit",font="verdana 10 bold", bg ="yellow",fg="blue",command=exit)
Exit.place(x=270,y=130)

clear=Button(root,text="Clear",font="verdana 10 bold", bg ="yellow",fg="blue",command=clear)
clear.place(x=170, y=130)

root.mainloop()
