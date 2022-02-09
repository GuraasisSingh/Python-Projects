#Loan Calculator
#monthly payment formula = (loan amount*monthly interest rate)/1-(1/(1+monthly interest years)**(no of years*12)
#Total payment= mp*12
from tkinter import *
root=Tk()
root.title("Loan Calculator")
root.geometry("500x450")
root.config(bg="gold")
def Calculate():
    aa=int(ae.get())
    nn=int(ne.get())
    ll=int(le.get())
    mit=aa/12
    monthlypay=(ll*mit)/(1-(1/(1+mit)**(nn*12)))
    totalpay=monthlypay*12
    Label(text=f"Monthly Payment\t{monthlypay}",font="verdana 8 bold").place(x=40,y=80)
    Label(text=f"Total Payment  \t{totalpay}",font="verdana 8 bold").place(x=40,y=100)

a=Label(root,text="Annual Interest Rate:",font="verdana 8 bold",bg="red",fg="white")
a.place(x=40,y=20)
n=Label(root,text="Number of Years:",font="verdana 8 bold",bg="red",fg="white")
n.place(x=40,y=40)
l=Label(root,text="Loan Amount:",font="verdana 8 bold",bg="red",fg="white")
l.place(x=40,y=60)

av=StringVar()
nv=StringVar()
lv=StringVar()

ae=Entry(root, font="verdana 8 bold",textvar=av,width=8,fg="black",bg="white")
ne=Entry(root, font="verdana 8 bold",textvar=nv,width=8,fg="black",bg="white")
le=Entry(root, font="verdana 8 bold",textvar=lv,width=8,fg="black",bg="white")

ae.place(x=180,y=20)
ne.place(x=180,y=40)
le.place(x=180, y=60)

b=Button(root, text="Compute Payment",font="arial 8",bg="red", fg="white",command=Calculate)
b.place(x=180,y=180)

root.mainloop()
