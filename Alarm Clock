#Alarm Clock
from tkinter import *
import datetime
import time
import winsound #python module ->built in  Based on output
from threading import *#emphasizing on getting values

root=Tk()
root.geometry("500x300")

def threading():
    t1=Thread(target=alarm)
    t1.start()

def alarm():
    while(True):
        setalarm=f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        currentTime=datetime.datetime.now().strftime("%H:%M:%S")
        if setalarm==currentTime:
            print("It's time to wake up")
            winsound.PlaySound('abc.wav',winsound.SND_FILENAME)
        
Label(root,text="Alarm Clock",bg='firebrick',fg='white',font=("Cosmic Sans MS",10,'bold')).pack(pady=15)
Label(root,text="Set Time",bg='firebrick',fg='white',font=("Cosmic Sans MS",10,'bold')).pack()
frame = Frame(root)
frame.pack()
hour=StringVar(root)
hours=("00","01","02",'03','04','05','10',"24")
hour.set(hours[0])
hrs=OptionMenu(frame,hour,*hours)
hrs.pack(side='left')

minute =StringVar(root)
minutes=("00","01","02",'03','04','05','14',"60")
minute.set(minutes[0])
mins=OptionMenu(frame,minute,*minutes)
mins.pack(side='left')

second =StringVar(root)
seconds=("00","01","02",'03','04','05',"60")
second.set(minutes[0])
secs=OptionMenu(frame,second,*seconds)
secs.pack(side='left')

Button(root,text="Set Alarm",bg='firebrick',fg='white',font=("Cosmic Sans MS",10,'bold'),command=threading).pack(pady=20)

root.mainloop()
