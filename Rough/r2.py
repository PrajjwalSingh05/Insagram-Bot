

def new_level():
    print(var.get())
from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x200')
ws.config(bg='#31403C')
var=IntVar()

sp=Spinbox(
    ws,
    textvariable=var,
    from_=1,
    to=10,
    font=('sans-serif', 14), 

).pack(pady=20)

    

b1=Button(ws,text="Button",command=new_level)
b1.pack()
ws.mainloop()