#Python IDLE using tkinter

from tkinter import *
root=Tk()
root.title("IDLE Shell 3.9.6")
root.geometry("500x500")
root.config(bg="white")
menu=Menu(root)
item1=Menu(menu)
item2=Menu(menu)
item3=Menu(menu)
item4=Menu(menu)
item5=Menu(menu)
item6=Menu(menu)
item7=Menu(menu)

menu.add_cascade(label="File",menu=item1)
item1.add_command(label="New File                    Ctrl+N")
item1.add_command(label="Open...                       Ctrl+O")
item1.add_command(label="Open Module...        Alt+M")
item1.add_command(label="Recent Files")
item1.add_command(label="Module Browser       Alt+C")
item1.add_command(label="Path Browser")
item1.add_separator()
item1.add_command(label="Save                           Ctrl+S")
item1.add_command(label="Save As...                   Ctrl+Shift+S")
item1.add_command(label="Save Copy As...         Alt+Shift+S")
item1.add_separator()
item1.add_command(label="Print Window           Ctrl+P")
item1.add_separator()
item1.add_command(label="Close                         Alt+F4")
item1.add_command(label="Exit                            Ctrl+Q")

menu.add_cascade(label="Edit",menu=item2)
item2.add_command(label="Undo                                     Ctrl+Z")
item2.add_command(label="Redo                                      Ctrl+Shift+Z")
item2.add_separator()
item2.add_command(label="Cut                                         Ctrl+X")
item2.add_command(label="Copy                                      Ctrl+C")
item2.add_command(label="Paste                                      Ctrl+V")
item2.add_command(label="Select All                                Ctrl+A")
item2.add_separator()
item2.add_command(label="Find...                                      Ctrl+F")
item2.add_command(label="Find Again                              Ctrl+G")
item2.add_command(label="Find Selection                        Ctrl+F3")
item2.add_command(label="Find in Files...                         Alt+F3")
item2.add_command(label="Replace                                   Ctrl+H")
item2.add_command(label="Go to Line                               Alt+G")
item2.add_command(label="Show Completions                Ctrl+space")
item2.add_command(label="Expand Word                          Alt+/")
item2.add_command(label="Show Call Tip                         Ctrl+backslash")
item2.add_command(label="Show Surrounding Parens    Ctrl+0")

menu.add_cascade(label="Format",menu=item3)
item3.add_command(label="Format Paragraph              Alt+Q")
item3.add_command(label="Indent Region                     Ctrl+]")
item3.add_command(label="Dedent Region                    Ctrl+[")
item3.add_command(label="Comment Out Region       Alt+3")
item3.add_command(label="Uncomment Region          Alt+4")
item3.add_command(label="Tabify Region                     Alt+5")
item3.add_command(label="Untabify Region                 Alt+6")
item3.add_command(label="Toggle Tabs                        Alt+T")
item3.add_command(label="New Indent Width             Alt+U")
item3.add_command(label="Strip Trailing Whitespace")

menu.add_cascade(label="Run",menu=item4)
item4.add_command(label="Run Module                F5")
item4.add_command(label="Run... Customized      Shift+F5")
item4.add_command(label="Check Module             Alt+X")
item4.add_command(label="Python Shell")

menu.add_cascade(label="Options",menu=item5)
item5.add_command(label="Configure IDLE")
item5.add_separator()
item5.add_command(label="Show Code Context")
item5.add_command(label="Show Line Numbers")
item5.add_command(label="Zoom Height                Alt+2")

menu.add_cascade(label="Windows",menu=item6)
item6.add_command(label="*IDLE Shell 3.9.6*")
item6.add_command(label="CY_36_HW.py - E:/GURAASIS/Python Codeyoung/CY_36_HW.py(3.9.6)")

menu.add_cascade(label="Help",menu=item7)
item7.add_command(label="About IDLE")
item7.add_separator()
item7.add_command(label="IDLE Help")
item7.add_command(label="Python Docs     F1")
item7.add_command(label="Turtle Demo")

root.config(menu=menu)

l1=Entry(root,bg="white",fg="black",width=100)
l1.grid(row=1,column=1)

root.mainloop()

