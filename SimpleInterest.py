from tkinter import *
root=Tk()
root.title("SI Calculator")
root.geometry("350x220")
root.config(bg="gold")
def Calculate():
    pp=int(pe.get())#get->gets value from entry boxes
    rr=int(re.get())
    tt=int(te.get())
    interest=(pp*rr*tt)/100
    Label(text=f"{interest}",font="verdana 10 bold").place(x=100,y=150)

    
p=Label(root,text="PRINCIPLE: ",font="verdana 8 bold",bg="red",fg="white").place(x=50, y=20)
r=Label(root,text="RATE: ",font="verdana 8 bold",bg="red",fg="white").place(x=50, y=40)
t=Label(root,text="TIME: ",font="verdana 8 bold",bg="red",fg="white").place(x=50, y=60)

pv=StringVar()
rv=StringVar()
tv=StringVar()

pe=Entry(root,font="verdana 8 bold",textvar=pv,width=8,bg="white",fg="black")
re=Entry(root,font="verdana 8 bold",textvar=rv,width=8,bg="white",fg="black")
te=Entry(root,font="verdana 8 bold",textvar=tv,width=8,bg="white",fg="black")

pe.place(x=130,y=20)
re.place(x=130,y=40)
te.place(x=130,y=60)

Button(root,text="Calculate",font="arial 10",bg="red",fg="white",command=Calculate).place(x=110,y=90)
Button(root,text="Exit",font="arial 10",bg="red",fg="white",command=lambda:exit()).place(x=200,y=90)#exits the program

root.mainloop()
