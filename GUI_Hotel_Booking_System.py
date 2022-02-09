#Gui of Hotel Booking System
from tkinter import *
root=Tk()
root.title("Hotel Booking System")
root.geometry("1000x1050")
root.config(bg="firebrick")

def  Calculate1():
    loc=location.get()
    if loc in ["Chandigarh", "Delhi", "Mumbai","Goa"]:
        s1=Label(root,text=f"The various hotels here a {loc} are:",fg="white",bg='firebrick',font=("Comic Sans MS", 10 ,"bold"))
        s1.place(x=40,y=130)
        s2=Label(root,text="Three Stars:\nCrown Palace, 2499 a night\nHilton Garden, 2800 a night\n Comfort Inn, 2000 a night",fg="white",bg='firebrick',font=("Comic Sans MS", 10 ,"bold"))
        s2.place(x=40,y=160)
        s3=Label(root,text="Four Stars:\nHoliday Inn, 3499 a night\nMandarian Garden, 6000 a night\n Peninsular Hotels, 8000 a night",fg="white",bg='firebrick',font=("Comic Sans MS", 10 ,"bold"))
        s3.place(x=300,y=160)
        s4=Label(root,text="Five Stars:\nHyatt, 2999 a night\nThe Breakers, 4000 a night\n Mariott International, 9000 a night",fg="white",bg='firebrick',font=("Comic Sans MS", 10 ,"bold"))
        s4.place(x=560,y=160)
        s5=Label(root,text="You will be served Complimentary breakfast in all the hotels",fg="white",bg='firebrick',font=("Comic Sans MS", 10 ,"bold"))
        s5.place(x=100,y=250)
        s6=Label(root,text="Enter 1 for Crown Palace, 2 for Hilton Garden, 3 for  Comfort Inn,\n4 for Holiday Inn,5 for Mandarian Garden 6 for Peninsular Hotels,\n 7 for Hyatt, 8 for The Breakers, 9 for  Mariott International",fg="white",bg='firebrick',font=("Comic Sans MS", 10 ,"bold"))
        s6.place(x=40,y=300)
        enter=StringVar
        global e1
        e1=Entry(root,textvar=enter,width=20,bg="chocolate",fg="white",font=("Cosmic Sans MS",10,'bold'))
        e1.place(x=500,y=300)
        calhotel=Button(root,text="Check Hotel Choice",bg="chocolate",fg='white',font=("Cosmic Sans MS",10,'bold'),command=Calculate2)
        calhotel.place(x=100,y=400)
    
    else:
        s=Label(root,text="Invalid Location. Please Enter a Valid Location.",fg="white",bg='firebrick',font=("Comic Sans MS", 10 ,"bold"))
        s.place(x=40,y=130)

def Calculate2():
    h=int(e1.get())
    if h in [1,2,3,4,5,6,7,8,9]:
        if h==1:
            p=2499
        elif h==2:
            p=2800
        elif h==3:
            p=2000
        elif h==4:
            p=3499
        elif h==5:
            p=6000
        elif h==6:
            p=8000
        elif h==7:
            p=2999
        elif h==8:
            p=4000
        elif h==9:
            p=9000
        print=Label(text=f"Thanks for using our platform to book, \n The total amount to be paid is Rs.{p}.",fg="white",bg='firebrick',height=4,font=("Comic Sans MS", 10 ,"bold"))
        print.place(x=100,y=450)
    else:
        invalid=Label(text="Invalid Choice.",fg="white",bg='firebrick',font=("Comic Sans MS", 10 ,"bold"),width=35,height=4)
        invalid.place(x=100,y=450)
    
 

def clear():    
    e1.delete(0, END)
    location.delete(0,END)
    
def exit():
    root.destroy()
    
welcome=Label(root,text="Welcome to our hotel booking system",fg="white",bg='firebrick',font=("Comic Sans MS", 15 ,"bold"))
welcome.place(x=200,y=10)
#font_tuple=("Comic Sans MS", 10 ,"bold")
#welcome.config(font=font_tuple)
enterLoc=Label(root,text="Enter location as Chandigarh, Delhi, Mumbai or Goa",fg="white",bg='firebrick',font=("Comic Sans MS", 10 ,"bold"))
enterLoc.place(x=10,y=60)

l=StringVar
location=Entry(root,textvar=l,width=20,bg="chocolate",fg="white",font=("Cosmic Sans MS",10,'bold'))
location.place(x=380,y=60)

calLoc=Button(root,text="Check Location",bg="chocolate",fg='white',font=("Cosmic Sans MS",10,'bold'),command=Calculate1)
calLoc.place(x=100,y=100)


Exit=Button(root,text="Exit",bg="chocolate",fg='white',font=("Cosmic Sans MS",10,'bold'),command=exit)
Exit.place(x=270, y=530)

clear=Button(root,text="Clear",bg="chocolate",fg='white',font=("Cosmic Sans MS",10,'bold'),command=clear)
clear.place(x=175, y=530)

root.mainloop()
