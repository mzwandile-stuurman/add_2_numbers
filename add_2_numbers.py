from tkinter import *

root = Tk()
root.geometry("500x250")# the size of the window
root.title("adding 2 numbers")

num1 = StringVar() #setting entries to be strings
num2 = StringVar()
results=StringVar()

def clear(): # function for clearing
    first_number.delete(0, END)
    second_number.delete(0, END)
    answer.config(state="normal")
    answer.delete(0,END)
    answer.config(state="readonly")


def add(): # the addition function
    number1 = int(first_number.get())
    answer.config(state="normal")
    number2= int(second_number.get())
    added = number1 + number2
    answer.delete(0,END)
    answer.insert(0, added) # display the sum value on the answer entry.
    answer.config(state="readonly")

def exit(): # the function to exit.
    root.destroy()



first_label = Label(root, text="Please Enter first Number")
first_number = Entry(root, textvariable = num1)


second_label = Label(root, text="Please Enter second Number")
second_number = Entry(root, textvariable= num2)

third_label = Label(root, text="Your answer")
answer = Entry(root, textvariable=results, state= "readonly")




btn1=Button(root, text= "ADD", command=add) # add functionality to the buttons
btn2=Button(root,text="Clear", command=clear)
btn3=Button(root,text= "Exit", command=exit)

first_label.place(x=0, y=0) # place the buttons
second_label.place(x=0, y=25)
third_label.place(x=0, y=50)
first_number.place(x=250, y=0)
second_number.place(x=250, y=25)
answer.place(x=250, y=50)

btn1.place(x=120, y=75) # place the buttons
btn2.place(x=180, y=75)
btn3.place(x=250, y=75)

root.mainloop() # make sure  the code shows




