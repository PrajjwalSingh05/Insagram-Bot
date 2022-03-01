
from tkinter import *
parent =Tk()
def new_level():
    new_le=Toplevel(parent,)
    b=Label(new_le,text="yuhi")
    b.place(x=0,y=0)
    new_le.grab_set()
    new_le.lift()
parent.geometry("300x300")
b1=Button(parent,text="Button",command=new_level)
b1.pack()
parent.mainloop()