from cProfile import label
from tkinter import *
parent=Tk()
# def change_tosecond():
#    first_frame.forget()
#    second_frame.place(x=0,y=0,height=500,width=500)
# def change_tofirst():
#    second_frame.forget()
#    first_frame.place(x=0,y=0,height=500,width=500)
# a=5
# first_frame=Frame(parent,bg="white", relief=GROOVE, borderwidth=5)
# first_frame.place(x=0,y=0,height=500,width=500)
# # first_frame.pack(fill="both",expand=1)
# second_frame=Frame(parent,bg="white", relief=GROOVE, borderwidth=5)
# # second_frame.place(x=500,y=500,height=500,width=500)
# first_button=Button(first_frame,text="First Frame",command=change_tosecond)
# first_button.place(x=0,y=0)

# second_button=Button(second_frame,text="second Frame",command=change_tofirst)
# second_button.place(x=50,y=60)
# first_label=Label(first_frame,text="This is first label")
# first_label.place(x=110,y=10)
# second_label=Label(second_frame,text="This is first label")
# second_label.place(x=110,y=110)
# # if a>0:
#     change_tosecond()
user=Text(parent,insertborderwidth=0.1)
user.place(x = 0, y = 20, height = 55, width = 200)
def h1():
   print(user.get(1.0, "end-1c"))
button1=Button(parent,text="Submit",command=h1)
button1.pack()
parent.mainloop()