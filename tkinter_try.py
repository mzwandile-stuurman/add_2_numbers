from tkinter import *
root = Tk() # created a blank window
myLabel= Label(root, text="Welcome to GUI design") #create an label object and position it within the root (main window)
myLabel.pack() #put the widget in the window and displays it
mytopFrame=Frame(root)#have added a top frame which is invisible
mytopFrame.pack()
mybottomframe=Frame(root)
mybottomframe.pack(side=BOTTOM) # just packing another invisible frame at the bottom
myaddButton3=Button(mytopFrame, text="Add", fg="red")# Positioning my button. takes 3 parameters (position, text and colour)
myaddButton3.pack(side=LEFT)
mysubButton=Button(mytopFrame, text="Subtract", fg="red")# Positioning my button. takes 3 parameters (position, text and colour)
mysubButton.pack(side=LEFT)
mymultiButton2=Button(mytopFrame, text="Multiply", fg="red")# Positioning my button. takes 3 parameters (position, text and colour)
mymultiButton2.pack(side=LEFT)

myexitButton4=Button(mybottomframe, text="Exit", fg="red")# Positioning my button. takes 3 parameters (position, text and colour)
myexitButton4.pack(side=BOTTOM)
root.mainloop() #to continuously display the GUI otherwise it flshes and disappears
