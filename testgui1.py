from tkinter import *
import os
import sys


root = Tk()

e = Entry(root, width=50,)
e.pack()


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

def myShellCmd():
    cmd = e.get()
    cmdString1 = cmd
    cmd = os.system(cmd)
    root.destroy()


myButton = Button(root, text="Enter  Your Name", command=myClick)
myButton.pack()


# myButton = Button(root, text="Enter  Your CMD to shell", command=myShellCmd)
# myButton.pack()



root.mainloop()

