from tkinter import *
import time
from PIL import ImageTk, Image
from functools import partial
from matplotlib.pyplot import title
from GUI import graphic,func

if __name__=="__main__":
  class Login_page:
        obj_function=func()

        obj=graphic()
# driver=init(driver)
        parent=Tk()
        max_size=600
        min_size=600
        parent.title("Linkdin Bot")
        width= parent.winfo_screenwidth() 
        height= parent.winfo_screenheight()
        parent.geometry("%dx%d" % (width, height))
        # parent.wm_attributes('-fullscreen', 'True')
        Title="Instagram Bot"
        title_box=obj.label(parent,Title)
        title_box.place(x=700,y=50)
#*********************************************************First Frame **********************************
        first_frame=obj.frame(parent)
        first_frame.place(x=150,y=200,height=500,width=500)
#*******************************Inserting image***************************************
        img = ImageTk.PhotoImage(Image.open("bot_pic.jpg"))
#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        panel = Label(first_frame, image = img)
#The Pack geometry manager packs widgets in rows or columns.
        panel.pack(side = "bottom", fill = "both", expand = "yes")
#****************************************************second frame*********************
        second_frame=obj.frame(parent)
        second_frame.place(x=900,y=200,height=500,width=600)

        
#**********************Username and Password **********************
        user_name=obj.label(second_frame,"USERNAME")
        user_name.place(x=0,y=90)
        entry_user_name=obj.entry_label(second_frame)
        entry_user_name.place(x=250,y=90)
        password=obj.label(second_frame,"PASSWORD")
        password.place(x=0,y=150)
        entry_password=obj.entry_label(second_frame)
        entry_password.place(x=250,y=150)
        login_button=obj.button(second_frame,"Login",partial(obj_function.login,entry_user_name,entry_password,parent))
        login_button.place(x=300,y=300)
        parent.mainloop()
        if obj_function.login_status==True:
            print("**********************************")
            print("yesyyesyeysyeysyers")
        #     obj_function.new_level(parent)
        else:
            print("**********************************")
            print("NO")