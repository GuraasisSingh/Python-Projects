#Build a Gui application to implement Pythagoras Theorem, Euclidean Distance and Manhattan Distance.
import math
from tkinter import *
root=Tk()
root.title("PROVING THEOREMS")
root.geometry("700x750")
root.config(bg="seagreen3")

def Calculate1():
    a=int(pe1.get())
    b=int(pe2.get())
    pyth=math.sqrt((a**2) + (b**2))
    c=Label(text=f"The hypotenuse is {pyth}",font="verdana 10 bold",bg="yellow2",fg="black")
    c.place(x=170, y=100)

def Calculate2():
    e1=int(ee1.get())
    e2=int(ee2.get())
    e3=int(ee3.get())
    e4=int(ee4.get())
    edis=math.sqrt(((e2-e1)**2)+((e4-e3)**2))
    Elud=Label(text=f"The Euclidean Distance is {edis}",font="verdana 10 bold",bg="yellow2",fg="black")
    Elud.place(x=170, y=300)

def Calculate3():
    x1=int(me1.get())
    x2=int(me2.get())
    y1=int(me3.get())
    y2=int(me4.get())
    dis1=abs(x2-x1)
    dis2=abs(y2-y1)
    mdis=dis1 +dis2 
    ManhD=Label(text=f"The Manhattan Distance is {mdis}",font="verdana 10 bold",bg="yellow2",fg="black")
    ManhD.place(x=170, y=500)

def clear():
    pe1.delete(0, END)
    pe2.delete(0, END)
    ee1.delete(0, END)
    ee2.delete(0, END)
    ee3.delete(0, END)
    ee4.delete(0, END)
    me1.delete(0, END)
    me2.delete(0, END)
    me3.delete(0, END)
    me4.delete(0, END)


def exit():
    root.destroy()


py=Label(root,text="Pythagoras Theorem",font="verdana 10 bold",bg="yellow2",fg="black")
py.place(x=150, y = 10)
ed=Label(root,text="Euclidean Distance",font="verdana 10 bold",bg="yellow2",fg="black")
ed.place(x=150, y = 150)
md=Label(root,text="Manhattan Distance",font="verdana 10 bold",bg="yellow2",fg="black")
md.place(x=150, y=350)


s1=Label(root,text="Enter side1 value:",font="verdana 10 bold",bg="yellow2",fg="black")
s1.place(x=40, y=40)
s2=Label(root,text="Enter side2 value:",font="verdana 10 bold",bg="yellow2",fg="black")
s2.place(x=40, y=70)
x1=Label(root,text="Enter x1 value:",font="verdana 10 bold",bg="yellow2",fg="black")
x1.place(x=40, y = 180)
x2=Label(root,text="Enter x2 value:",font="verdana 10 bold",bg="yellow2",fg="black")
x2.place(x=40, y = 210)
y1=Label(root,text="Enter y1 value:",font="verdana 10 bold",bg="yellow2",fg="black")
y1.place(x=40, y=240)
y2=Label(root,text="Enter y2 value:",font="verdana 10 bold",bg="yellow2",fg="black")
y2.place(x=40, y=270)
mx1=Label(root,text="Enter x1 value:",font="verdana 10 bold",bg="yellow2",fg="black")
mx1.place(x=40, y = 380)
mx2=Label(root,text="Enter x2 value:",font="verdana 10 bold",bg="yellow2",fg="black")
mx2.place(x=40, y = 410)
my1=Label(root,text="Enter y1 value:",font="verdana 10 bold",bg="yellow2",fg="black")
my1.place(x=40, y=440)
my2=Label(root,text="Enter y2 value:",font="verdana 10 bold",bg="yellow2",fg="black")
my2.place(x=40, y=470)

ps1=StringVar()
ps2=StringVar()
es1=StringVar()
es2=StringVar()
es3=StringVar()
es4=StringVar()
ms1=StringVar()
ms2=StringVar()
ms3=StringVar()
ms4=StringVar()

pe1=Entry(root,font="verdana 10 bold",textvar=ps1,width=8,bg="yellow2",fg="black")
pe1.place(x=230,y=40)
pe2=Entry(root,font="verdana 10 bold",textvar=ps2,width=8,bg="yellow2",fg="black")
pe2.place(x=230,y=70)
ee1=Entry(root,font="verdana 10 bold",textvar=es1,width=8,bg="yellow2",fg="black")
ee1.place(x=230,y=180)
ee2=Entry(root,font="verdana 10 bold",textvar=es2,width=8,bg="yellow2",fg="black")
ee2.place(x=230,y=210)
ee3=Entry(root,font="verdana 10 bold",textvar=es3,width=8,bg="yellow2",fg="black")
ee3.place(x=230,y=240)
ee4=Entry(root,font="verdana 10 bold",textvar=es4,width=8,bg="yellow2",fg="black")
ee4.place(x=230,y=270)
me1=Entry(root,font="verdana 10 bold",textvar=ms1,width=8,bg="yellow2",fg="black")
me1.place(x=230,y=380)
me2=Entry(root,font="verdana 10 bold",textvar=ms2,width=8,bg="yellow2",fg="black")
me2.place(x=230,y=410)
me3=Entry(root,font="verdana 10 bold",textvar=ms3,width=8,bg="yellow2",fg="black")
me3.place(x=230,y=440)
me4=Entry(root,font="verdana 10 bold",textvar=ms4,width=8,bg="yellow2",fg="black")
me4.place(x=230,y=470)


cal1=Button(root,text="Calculate",font="verdana 10 bold",bg="yellow2",fg="black",command=Calculate1)
cal1.place(x=40,y=100)
cal2=Button(root,text="Calculate",font="verdana 10 bold",bg="yellow2",fg="black",command=Calculate2)
cal2.place(x=40,y=300)
cal3=Button(root,text="Calculate",font="verdana 10 bold",bg="yellow2",fg="black",command=Calculate3)
cal3.place(x=40, y=500)


Exit=Button(root,text="Exit",font=("verdana",10,"bold"),bg="yellow2",fg="black",command=exit)
Exit.place(x=270, y=550)

clear=Button(root,text="Clear",font=("verdana",10,"bold"),bg="yellow2",fg="black",command=clear)
clear.place(x=175, y=550)

root.mainloop()
