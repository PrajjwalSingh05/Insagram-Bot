from distutils import command
import imp
from mimetypes import init
from tkinter import *
from tkinter import messagebox
import urllib
import requests
import webdriver_manager
import time
import pandas as pd
from bs4 import BeautifulSoup
from typing import Text
from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class graphic:
    font_name="Times"
    font_size=24
   
    def button(self,parent,user_text,commands=None):
        button_name=Button(parent,text=user_text,bg="white",relief=GROOVE,borderwidth=5,font=(self.font_name,self.font_size),command=commands)
        return button_name
    def frame(self,parent):
        new_frame=Frame(parent,bg="white",relief=GROOVE,borderwidth=5)
        return new_frame
    def label(self,parent,user_text):
        new_label=Label(parent,bg="white",relief=GROOVE,borderwidth=5,text=user_text,font=(self.font_name,self.font_size))
        return new_label
    def entry_label(self,parent):
        new_entry=Entry(parent,bg="white",relief=GROOVE,borderwidth=5,font=(self.font_name,self.font_size))
        return new_entry

class func:
    login_status=False
    def new_level(self,parent):
        print("****************")
        print("****************")
        new_state=Toplevel(parent)

        
    
    def init(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.instagram.com/")
        print("inside driver")
        time.sleep(1)
        return driver
    def login(self,username,password,parent):
        try:
    #         user_name="tester05032002@gmail.com"
    # password="9450752717"
            user_name=username.get()
            user_password=password.get()
            if user_name=="" or user_password=="":
                messagebox.showerror("Error","All Field required")
            else:
                driver=self.init()
                user_path=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
                user_path.send_keys(user_name)
                password_path=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
                password_path.send_keys(user_password)
                login_button=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
                login_button.click()
                time.sleep(10)
                not_now_option=driver.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button")
                not_now_option.click()
                time.sleep(5)
                remember_me_option=driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
                remember_me_option.click()
                time.sleep(5)
                self.login_status=messagebox.askyesno("Login Sucessfull","Are u sure to login")
                print("////////////////////////////////")
                print("////////////////////////////////")
                print(self.login_status)
                driver.close()
                if self.login_status==True:
                    print("**********************************")
                    print("yesyyesyeysyeysyers")
                    self.new_level(parent)

        except Exception as ep:
            print(f"Error, Error due to {str(ep)}")


            
         
