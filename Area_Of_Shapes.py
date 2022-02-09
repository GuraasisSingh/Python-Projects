#Build a Gui application to compute area of different shapes 
import math
from tkinter import *
root=Tk()
root.title("SHAPE CALCULATOR")
root.geometry("600x550")
root.config(bg="yellow")

def Calculate1():
    si=int(Esq.get())
    sq=si**2
    sqAr=Label(text=f"The area of square is {sq}",font="verdana 10 bold",bg="red",fg="white")
    sqAr.place(x=170, y=70)

def Calculate2():
    rec1=int(Ere1.get())
    rec2=int(Ere2.get())
    rec=rec1*rec2
    recAr=Label(text=f"The area of rectangle is {rec}",font="verdana 10 bold",bg="red",fg="white")
    recAr.place(x=170, y=210)

def Calculate3():
    tri1=int(Et1.get())
    tri2=int(Et2.get())
    tri3=int(Et3.get())
    s=(tri1+tri2+tri3)/2
    tri=math.sqrt((s*(s-tri1)*(s-tri2)*(s-tri3)))
    triAr=Label(text=f"The area of triangle is {tri}",font="verdana 10 bold",bg="red",fg="white")
    triAr.place(x=170, y=380)

def clear():
    Esq.delete(0, END)
    Ere1.delete(0, END)
    Ere2.delete(0, END)
    Et1.delete(0, END)
    Et2.delete(0, END)
    Et3.delete(0, END)


def exit():
    root.destroy()


sh1=Label(root,text="Square",font="verdana 10 bold",bg="red",fg="white")
sh1.place(x=150, y = 10)
sh2=Label(root,text="Rectangle",font="verdana 10 bold",bg="red",fg="white")
sh2.place(x=150, y = 120)
sh3=Label(root,text="Triangle",font="verdana 10 bold",bg="red",fg="white")
sh3.place(x=150, y=260)


side1=Label(root,text="Enter side value:",font="verdana 10 bold",bg="red",fg="white")
side1.place(x=40, y=40)
rside1=Label(root,text="Enter side1 value:",font="verdana 10 bold",bg="red",fg="white")
rside1.place(x=40, y = 150)
rside2=Label(root,text="Enter side2 value:",font="verdana 10 bold",bg="red",fg="white")
rside2.place(x=40, y = 180)
tside1=Label(root,text="Enter side1 value:",font="verdana 10 bold",bg="red",fg="white")
tside1.place(x=40, y=290)
tside2=Label(root,text="Enter side2 value:",font="verdana 10 bold",bg="red",fg="white")
tside2.place(x=40, y=320)
tside3=Label(root,text="Enter side3 value:",font="verdana 10 bold",bg="red",fg="white")
tside3.place(x=40, y=350)

s1=StringVar()
sr1=StringVar()
sr2=StringVar()
ts1=StringVar()
ts2=StringVar()
ts3=StringVar()


Esq=Entry(root,font="verdana 10 bold",textvar=s1,width=8,bg="red",fg="white")
Esq.place(x=230,y=40)
Ere1=Entry(root,font="verdana 10 bold",textvar=sr1,width=8,bg="red",fg="white")
Ere1.place(x=230,y=150)
Ere2=Entry(root,font="verdana 10 bold",textvar=sr2,width=8,bg="red",fg="white")
Ere2.place(x=230,y=180)
Et1=Entry(root,font="verdana 10 bold",textvar=ts1,width=8,bg="red",fg="white")
Et1.place(x=230,y=290)
Et2=Entry(root,font="verdana 10 bold",textvar=ts2,width=8,bg="red",fg="white")
Et2.place(x=230,y=320)
Et3=Entry(root,font="verdana 10 bold",textvar=ts3,width=8,bg="red",fg="white")
Et3.place(x=230,y=350)


cal1=Button(root,text="Calculate",font="verdana 10 bold",bg="red",fg="white",command=Calculate1)
cal1.place(x=40,y=70)
cal2=Button(root,text="Calculate",font="verdana 10 bold",bg="red",fg="white",command=Calculate2)
cal2.place(x=40,y=210)
cal3=Button(root,text="Calculate",font="verdana 10 bold",bg="red",fg="white",command=Calculate3)
cal3.place(x=40, y=380)


Exit=Button(root,text="Exit",font=("verdana",10,"bold"),bg="red",fg="white",command=exit)
Exit.place(x=270, y=450)

clear=Button(root,text="Clear",font=("verdana",10,"bold"),bg="red",fg="white",command=clear)
clear.place(x=175, y=450)

root.mainloop()
