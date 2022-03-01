from tkinter import *
import time
from PIL import ImageTk, Image
from functools import partial
# from matplotlib.pyplot import title
from GUI import Graphic,Func
from function_gui import Func_graphic

if __name__=="__main__":
  class Login_page:
 #***************************************object of CLass function*************************************
        obj_function=Func()

        obj_graphic=Graphic()
# **********************object of function gui page(func_graphic class)*******************************
        obj_function_gui=Func_graphic(False)
# driver=init(driver)
        parent=Tk()
        max_size=600
        min_size=600
        parent.title("Linkdin Bot")
        width= parent.winfo_screenwidth() 
        height= parent.winfo_screenheight()
        parent.geometry("%dx%d" % (width, height))
        parent.config(bg="#05716c")
        parent.wm_attributes('-fullscreen', 'True')
        Title="Instagram Bot"
        title_box=obj_graphic.label(parent,Title)
        title_box.place(x=700,y=50)
#*********************************************************First Frame **********************************
        first_frame=obj_graphic.frame(parent)
        first_frame.place(x=150,y=200,height=500,width=500)
#*******************************Inserting image***************************************
        img = ImageTk.PhotoImage(Image.open("Bot_pic.jpg"))
#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        panel = Label(first_frame, image = img)
#The Pack geometry manager packs widgets in rows or columns.
        panel.pack(side = "bottom", fill = "both", expand = "yes")
#****************************************************second frame*********************
        second_frame=obj_graphic.frame(parent)
        second_frame.place(x=900,y=200,height=500,width=600)

        
#**********************Username and Password **********************
        user_name=obj_graphic.label(second_frame,"USERNAME")
        user_name.place(x=0,y=90)
        entry_user_name=obj_graphic.entry_label(second_frame)
        entry_user_name.place(x=250,y=90)
        password=obj_graphic.label(second_frame,"PASSWORD")
        password.place(x=0,y=150)
        entry_password=obj_graphic.entry_label(second_frame)
        entry_password.place(x=250,y=150)
        # login_button=obj.button(second_frame,"Login",command=parent.destroy)
        # login_button=obj.button(second_frame,"Login",(lambda:obj_function.login(entry_user_name,entry_password,parent)))
        login_button=obj_graphic.button(second_frame,"Login",partial(obj_function.login,entry_user_name,entry_password,parent))
        login_button.place(x=300,y=300)
        quit_button=obj_graphic.button(parent,"quit",parent.quit)
        quit_button.place(x=600,y=300)
        function_button=obj_graphic.button(parent,"Function",partial(obj_function_gui.function_page))
        function_button.place(x=550,y=200)
        parent.mainloop()
        if obj_function.login_status==True:
            print("**********************************")
            print("yesyyesyeysyeysyers")
        #     obj_function.new_level(parent)
        else:
            print("**********************************")
            print("NO")