from tkinter import *
root=Tk()
root.title("CALCULATOR")
root.geometry("400x650")
root.config(bg="light blue")

operator=""
text_input=StringVar()
textDisplay=Entry(root,font=("arial",20,"bold"),textvariable=text_input,bd=30,insertwidth=4,bg="powder blue",justify="right").grid(columnspan=6)

def click(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)

def clear():
    global operator
    operator=""
    text_input.set("")

def equals():
    global operator
    sumup=str(eval(operator))  
    text_input.set(sumup)
    operator=""

b1=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="^",command=lambda:click("**")).grid(row=7,column=0)
b2=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="0",command=lambda:click(0)).grid(row=7,column=1)
b3=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text=".",command=lambda:click(".")).grid(row=7,column=2)
b4=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="=",command=lambda:equals()).grid(row=7,column=3)
b5=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="1",command=lambda:click(1)).grid(row=6,column=0)
b6=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="2",command=lambda:click(2)).grid(row=6,column=1)
b7=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="3",command=lambda:click(3)).grid(row=6,column=2)
b8=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="+",command=lambda:click("+")).grid(row=6,column=3)
b9=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="4",command=lambda:click(4)).grid(row=5,column=0)
b10=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="5",command=lambda:click(5)).grid(row=5,column=1)
b11=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="6",command=lambda:click(6)).grid(row=5,column=2)
b12=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="-",command=lambda:click("-")).grid(row=5,column=3)
b13=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="7",command=lambda:click(7)).grid(row=4,column=0)
b14=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="8",command=lambda:click(8)).grid(row=4,column=1)
b15=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="9",command=lambda:click(9)).grid(row=4,column=2)
b16=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="x",command=lambda:click("*")).grid(row=4,column=3)
b17=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="÷",command=lambda:click("/")).grid(row=3,column=3)
b18=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="C",command=lambda:clear()).grid(row=3,column=0)
b19=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text="(",command=lambda:click("(")).grid(row=3,column=1)
b20=Button(root,padx=20,pady=20,bd=8,fg="black",font=("arial",18,"bold"),bg="cadet blue",text=")",command=lambda:click(")")).grid(row=3,column=2)

root.mainloop()
