from tkinter import *
root=Tk()
root.title()
root.title("CI Calculator")
root.geometry("500x550")
root.config(bg="gold")
def Calculate():
    pg=int(pe.get())
    rg=int(re.get())
    tg=int(te.get())
    ci=(pg*((1+(rg/100))**tg))-pg
    Label(text=f"{ci}",font="arial 10").place(x=100,y=160)

p=Label(root,text="PRINCIPLE: ",font="arial 10",bg="green",fg="white").place(x=50,y=10)
r=Label(root,text="RATE        : ",font="arial 10",bg="green",fg="white").place(x=50,y=30)
t=Label(root,text="TIME         : ",font="arial 10",bg="green",fg="white").place(x=50,y=50)

pv=StringVar()
rv=StringVar()
tv=StringVar()

pe=Entry(root,font="arial 10",textvar=pv,width=8,bg="white",fg="black")
re=Entry(root,font="arial 10",textvar=rv,width=8,bg="white",fg="black")
te=Entry(root,font="arial 10",textvar=tv,width=8,bg="white",fg="black")

pe.place(x=140, y=10)
re.place(x=140, y=30)
te.place(x=140, y=50)

Button(root,text="Calculation",font="arial 10",bg="firebrick1", fg="white",command=Calculate).place(x=100,y=90)
Button(root,text="Exit",font="arial 10",bg="firebrick1", fg="white",command=lambda:exit()).place(x=200,y=90)


root.mainloop()
