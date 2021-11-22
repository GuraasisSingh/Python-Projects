from tkinter import *
import calendar
root=Tk()
root.geometry("500x550")
root.title("CALENDAR")
root.config(bg="limegreen")

def show():
    m=int(month.get())
    y=int(year.get())
    o=calendar.month(y,m)
    cal.insert("end",o)

def clear():
    cal.delete('1.0', END)

def exit():
    root.destroy()

m_label=Label(root,text="Month",font=("verdana","10","bold"))
m_label.place(x=20,y=50)

month=Spinbox(root,from_=1,to=12,width="2")
month.place(x=80,y=50)

y_label=Label(root,text="Year",font=("verdana","10","bold"))
y_label.place(x=120,y=50)

year=Spinbox(root,from_=1800,to=3000,width="5")
year.place(x=170,y=50)

cal=Text(root,width=21,height=6,borderwidth=2)
cal.place(x=50, y=110)

show=Button(root,text="Show",font=("verdana",8,"bold"),command=show)
show.place(x=20, y=250)

Exit=Button(root,text="Exit",font=("verdana",8,"bold"),command=exit)
Exit.place(x=170, y=250)


clear=Button(root,text="Clear",font=("verdana",8,"bold"),command=clear)
clear.place(x=100, y=250)

root.mainloop()
