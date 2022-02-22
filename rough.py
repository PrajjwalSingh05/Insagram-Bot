from multiprocessing import parent_process
from tkinter import *
def newlevel():
    a=Toplevel(parent)
parent =Tk()
button=Button(parent,text="button").place(x=0,y=0)
# a=int(input("Enter a number"))
# if a==1:
#     newlevel()

button2=Button(parent,text="button2",command=parent.destroy).place(x=10,y=10)
parent.mainloop()