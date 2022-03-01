from tkinter import *
from PIL import ImageTk, Image
from functools import partial
from tkinter import messagebox

#******************User defined Libary******************************
from GUI import Graphic,Func
#*******************************Object of functions*************
obj_function=Func()
#****************************Object of graphic class ********************************
obj_graphic=Graphic()

class Func_graphic:
        obj_function.login_status=False
        login=False    
        def __init__(self,val):
                print("***************")
                print("***************")
                print("The value of val is ",val)
                self.login=val
        def function_page(self):
                print("*************")
                print("*************")
                # print(obj_function.login_status)
                if self.login==False:
                # if obj_function.login_status==True:
                        parent=Tk()
                        max_size=600
                        min_size=600
                        parent.title("Linkdin Bot")
                        width= parent.winfo_screenwidth() 
                        height= parent.winfo_screenheight()
                        parent.geometry("%dx%d" % (width, height))
                        parent.config(bg="#05716c")
                        #parent.wm_attributes('-fullscreen', 'True')
                        Title="Instagram Bot"
                        title_box=obj_graphic.label(parent,Title)
                        title_box.place(x=700,y=50)
                #*********************************************************First Frame **********************************
                        first_frame=obj_graphic.frame(parent)
                        first_frame.place(x=150,y=200,height=500,width=500)
                #*******************************Inserting image***************************************
                        # img = ImageTk.PhotoImage(Image.open("bot_pic.jpg"))
                        # print("********************")
                        # print("PIc readed")
                        # print("********************")
                #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
                        # panel = Label(first_frame, image = img)
                        # print("********************")
                        # print("PAnel done")
                        # print("********************")
                #The Pack geometry manager packs widgets in rows or columns.
                        # panel.pack(side = "bottom", fill = "both", expand = "yes")
                #****************************************************second frame*********************
                        second_frame=obj_graphic.frame(parent)
                        second_frame.place(x=900,y=200,height=500,width=600)
                #*************************************Function Button *************************************
                        request_buton=obj_graphic.button(second_frame,"Send Request",partial(obj_function.request_level,parent,))
                        request_buton.place(x=0,y=0)
                        send_message_buton=obj_graphic.button(second_frame,"Send Message",partial(obj_function.send_message_level,parent))
                        send_message_buton.place(x=300,y=0)
                        save_profile_pic_button=obj_graphic.button(second_frame,"Save Profile Pic",partial(obj_function.save_profilepic_level,parent))
                        save_profile_pic_button.place(x=0,y=150)
                        send_message_buton.place(x=300,y=0)
                        save_posts_button=obj_graphic.button(second_frame,"Save Posts",partial(obj_function.save_posts_level,parent))
                        save_posts_button.place(x=300,y=150)
                        quit_button=obj_graphic.button(parent,"quit",parent.destroy)
                        quit_button.place(x=600,y=300)
                        parent.lift()
                        # parent.attributes("-topmost", True)
                        parent.mainloop()
                else:
                         messagebox.showerror("Error ","Please Login First")

