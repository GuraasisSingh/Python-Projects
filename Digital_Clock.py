#Digital clock
from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title("Clock")

def time():
    string=strftime("%H:%M:%S:%p")#format codes as argument.
    l.config(text=string)
    l.after(1000,time)

l=Label(root,font=("calibri",50,"bold"),background="purple",foreground="white")
l.pack(anchor="ne")
time()

root.mainloop()
