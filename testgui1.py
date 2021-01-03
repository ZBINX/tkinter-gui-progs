from tkinter import *
import os

### Main Window but hidden from view
root = Tk()
root.withdraw()


### Top level window called nameWindow, resides on top of main root window ( in view)
nameWindow = Toplevel(root)
nameWindow.title("Enter Your Name")


### Nick Name window but hidden from view until called
nickNameWin = Toplevel(nameWindow)
nickNameWin.withdraw()




### Functions
#def nameForget():
#    nameInput.pack_forget()



def nameClick():
    name = nameInput.get()
    openWin2()
    
    
def openWin2():
    nickNameWin = Toplevel(nameWindow)
    nickNameWin.title("Enter your nickname")
    ### Remove previous name window
    nameWindow.withdraw()
    ### Text box to input your nickname
    nameInput = Entry(nickNameWin, width=50,)
    nameInput.pack()
    ### button to enter your nickname
    nameButton = Button(nickNameWin, text="Enter your Nickname", command=openWin3)
    nameButton.pack()
    ### button to close program
    closeButton = Button(nickNameWin, text="Exit program", command=closeProg)
    closeButton.pack()
    


def nickNameClick():
	nickName = nickNameInput.get()
	myNickNamePopup = Label(nickNameWin, text=name)
	myNickNamePopup.pack()

def closeProg():
	root.destroy()

def openWin3():
	ageWin = Toplevel(nickNameWin)
	ageWin.title("Enter your age!")

	nickNameWin.withdraw()

	nameInput = Entry(ageWin, width=50,)
	nameInput.pack()

	nameButton = Button(ageWin, text="Submit Age", command=closeProg)
	nameButton.pack()

	closeButton = Button(ageWin, text="Exit Program")
	closeButton.pack()


    


### Text box for user input
nameInput = Entry(nameWindow, width=50,)
nameInput.pack()

#nickNameInput = Entry(nickNameWin, width=50,)
#nickNameInput.pack()

### Buttons
nameButton = Button(nameWindow, text="Enter your name", command=nameClick)
nameButton.pack()

closeButton = Button(nameWindow, text="Close Window", command=closeProg)
closeButton.pack()



#nickNameInput = Entry(nameWindow, width=50,)
#nickNameInput.pack()

#nickNameButton = Button(window2, text="Enter your Nickname", command=nickNameClick)
#nickNameButton.pack()


# popup1 = Toplevel()
#popup1.title(name + "  is now stored as name")
#popup1.pack()



# myButton = Button(root, text="Enter  Your CMD to shell", command=myShellCmd)
# myButton.pack()

#def myShellCmd():
#    cmd = e.get()
#    cmdString1 = cmd
#    cmd = os.system(cmd)
#    

#def closeWin2():
#    nickNameWin.withdraw()
#    root.destroy()
#
#

root.mainloop()