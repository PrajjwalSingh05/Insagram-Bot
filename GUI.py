from distutils import command
from statistics import median

from tkinter import *
from tkinter import messagebox
from turtle import color
import urllib
from cv2 import blur

from matplotlib import widgets
import requests
import webdriver_manager
import time
import pandas as pd
from bs4 import BeautifulSoup
from typing import Text
from functools import partial
#*************************Build in Lib for Selinium*************************
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class Graphic:
    color_theme="slate blue"
    font_name = "Times"
    font_size = 24

    def button(self, parent, user_text, commands=None):
        button_name = Button(parent, text=user_text,  relief=GROOVE, borderwidth=5, font=(
            self.font_name, self.font_size), bg=self.color_theme ,  command=commands)
        return button_name

    def frame(self, parent):
        new_frame = Frame(parent, bg="white", relief=GROOVE, borderwidth=5)
        return new_frame

    def label(self, parent, user_text):
        new_label = Label(parent, relief=GROOVE, borderwidth=5,
                          text=user_text, font=(self.font_name, self.font_size),bg=self.color_theme )
        return new_label

    def entry_label(self, parent):
        new_entry = Entry(parent, bg="white", relief=GROOVE,
                          borderwidth=5, font=(self.font_name, self.font_size))
        return new_entry
    def Text(self,parent):
        new_text=Text(parent,)
        return new_text


class Func:
    min_sleep=3
    max_sleep=10
    mid_sleep=5
    global login_info
    login_info = True
    login_status = True
    # login_status = login_info
    obj_graphic=Graphic()
    
    def new_level(self,parent):
        new_level=Toplevel(parent)
        new_level.geometry("300x300")
        new_level.grab_set()
        return new_level

    def request_level(self, parent):
        pop_up_level=self.new_level(parent)
        username=self.obj_graphic.label(pop_up_level,"UserId")
        username.place(x=10,y=10)
        entry_username=self.obj_graphic.entry_label(pop_up_level)
        entry_username.place(x=130,y=0)
        quit_button=self.obj_graphic.button(pop_up_level,"quit",pop_up_level.destroy)
        quit_button.place(x=150,y=200)
        submit_button=self.obj_graphic.button(pop_up_level,"Submit",partial(self.send_request,entry_username))
        # submit_button=self.obj_graphic.button(pop_up_level,"Submit",partial(self.send_request,entry_username))
        submit_button.place(x=150,y=150)
#*************************************Function to Send Request**********************************************************
    def send_request(self,request_name):
        try:
            driver.maximize_window()
            driver.get("https://www.instagram.com/")
            time.sleep(3)
            search_box=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
            # request_name="python.learning"
            search_box.send_keys(request_name.get())
            time.sleep(5)
            insta_id=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div")
        
            insta_id.click()
            follow_button=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button/div')))
            follow_button.click()
            driver.minimize_window()
            messagebox.showinfo("Task Completed","Request sent")
        except Exception as es:
            print("Exception occured")
            messagebox.showerror(" Error","NEtwork Error")
#*******************************************************Send Message *******************************
    def send_message_level(self, parent):
        pop_up_level=self.new_level(parent)
        username=self.obj_graphic.label(pop_up_level,"UserId")
        username.place(x=10,y=10)
        entry_username=self.obj_graphic.entry_label(pop_up_level)
        entry_username.place(x=130,y=0)
        send_text_message=self.obj_graphic.entry_label(pop_up_level)
        send_text_message.place(x = 100, y = 50,height=50,width=300)
        submit_button=self.obj_graphic.button(pop_up_level,"Submit",partial(self.send_message,entry_username,send_text_message))
        # submit_button=self.obj_graphic.button(pop_up_level,"Submit",partial(self.send_request,entry_username))
        submit_button.place(x=150,y=150)
        quit_button=self.obj_graphic.button(pop_up_level,"quit",pop_up_level.destroy)
        quit_button.place(x=150,y=200)
    def send_message(self,username,text):
        try:
            driver.maximize_window()
            driver.get("https://www.instagram.com/")
        
            message_icon=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')))
            message_icon.click()
        
            send_message_icon=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button')))
            send_message_icon.click()
            
            to_search_box=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input')))
            message_name=username.get()
            to_search_box.send_keys(message_name)
            time.sleep(2)
        

            name_searched=driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div")
            name_searched.click()
            
            next_button=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div/div/div[1]/div/div[2]/div/button/div')))
            next_button.click()
        
            text_message=text.get()
        
            insert_message=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')))
            insert_message.send_keys(text_message)
            time.sleep(self.min_sleep)
            send_button=driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
            send_button.click()
            driver.minimize_window()
            messagebox.showinfo("Task Completed","message Sent")
        except Exception as es:
            messagebox.showerror(" Error","NEtwork Error")
        finally:
            top
    def save_posts_level(self,parent):
        pop_up_level=self.new_level(parent)
        username=self.obj_graphic.label(pop_up_level,"UserId")
        username.place(x=10,y=10)
        entry_username=self.obj_graphic.entry_label(pop_up_level)
        entry_username.place(x=130,y=0)
        quit_button=self.obj_graphic.button(pop_up_level,"quit",pop_up_level.destroy)
        quit_button.place(x=10,y=170)
        global var
        var=IntVar()
        sp=Spinbox( pop_up_level, textvariable=var, from_=1, to=10,font=('sans-serif', 14), )
        sp.place(x=60,y=100) 
        submit_button=self.obj_graphic.button(pop_up_level,"Submit",partial(self.save_posts,entry_username))

        submit_button.place(x=150,y=170)
        # submit_button=self.obj_graphic.button(pop_up_level,"Submit",partial(self.send_request,entry_username))
    def save_posts(self,request_id):
        try:
            driver.maximize_window()
            i=1
            no_of_post=var.get()
            print("**************************")
            print("**************************")
            print(no_of_post)
            print(type(no_of_post))
            driver.get("https://www.instagram.com/")
            search_box=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
            request_name=request_id.get()
            search_box.send_keys(request_name)
            time.sleep(2)
            insta_id=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div")
            
            insta_id.click()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(6)
            body=driver.find_element_by_tag_name("body")
            page=body.get_attribute("innerHTML")
            soup=BeautifulSoup(page,"html.parser")
            time.sleep(5)
            userimage=soup.find_all("img")
            # if not userimage:
            #     print("*******************************")
            for j in range(0,5):
                element=userimage[j]
                print(element)
                url=element["src"]
                pic_name="post"
                urllib.request.urlretrieve(url,("Saved_Posts/" +pic_name+str(i)+".png"))
                i=i+1
            driver.minimize_window()
            messagebox.showinfo("Task Completed","Post saved")
        except Exception as es:
            messagebox.showerror(" Error","NEtwork Error")

            
    def save_profilepic_level(self,parent):
        pop_up_level=self.new_level(parent)
        username=self.obj_graphic.label(pop_up_level,"UserId")
        username.place(x=10,y=10)
        entry_username=self.obj_graphic.entry_label(pop_up_level)
        entry_username.place(x=130,y=0)
        quit_button=self.obj_graphic.button(pop_up_level,"quit",pop_up_level.destroy)
        quit_button.place(x=150,y=200)
        submit_button=self.obj_graphic.button(pop_up_level,"Submit",partial(self.save_profile,entry_username,pop_up_level,parent))
        # submit_button=self.obj_graphic.button(pop_up_level,"Submit",partial(self.send_request,entry_username))
        submit_button.place(x=150,y=150)
    def save_profile(self,username,pop_up_level,parent):
        try:
            driver.maximize_window()
            driver.get("https://www.instagram.com/")
            search_box=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
            request_name=username.get()
            search_box.send_keys(request_name)
            time.sleep(self.min_sleep)
            insta_id=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div")
            insta_id.click()
            time.sleep(self.min_sleep)
            body=driver.find_element_by_tag_name("body")
            page=body.get_attribute("innerHTML")
            soup=BeautifulSoup(page,"html.parser")
            userimage=soup.select('img[alt="'+request_name+'\'s profile picture"]')
        # userimage=soup.select('._6q-tv')
            if not userimage:
                print("***************************************")
                userimage=soup.select('.be6sR')
            url=userimage[0]["src"]
            urllib.request.urlretrieve(url,"Saved_Profile_pic/userprofile.jpg")
            driver.minimize_window()
            messagebox.showinfo("Task Completed","Profile Pic Saved ")
        except Exception as es:
            print(es)
            messagebox.showerror(" Error","NEtwork Error")
        finally:
            pop_up_level.quit()
            parent.lift()
            

        

    def init(self):
        global driver 
        driver= webdriver.Chrome("D:/Project/New folder/Instagram_Bot/Chromedriver.exe")
        driver.get("https://www.instagram.com/")
        print("inside driver")
        time.sleep(1)
        return driver
#*************************************Function to Login*******************************************************
    def login(self, username, password, parent):
        try:
            # user_name="tester05032002@gmail.com"
            # password="9450752717"
            user_name = username.get()
            user_password = password.get()
            if user_name == "" or user_password == "":
                messagebox.showerror("Error", "All Field required")
            else:
                driver = self.init()
                user_path = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
              
                user_path.send_keys(user_name)
                password_path = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
                
                password_path.send_keys(user_password)
                
                login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')))
               
                login_button.click()

                not_now_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
                not_now_option.click()
                time.sleep(self.min_sleep)
                remember_me_option=driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
                remember_me_option.click()
                # remember_me_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                #     (By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')))
                # remember_me_option.click()
        
                login_info=True
                self.login_status=True
                print("*********************")
                print("*********************")
                print(self.login_status)
                driver.minimize_window()
                obj_function_gui=Func_graphic(True)
                self.login_status = messagebox.askyesno(
                    "Login Sucessfull", "Are u sure to login")
               # driver.close()
               
        except Exception as ep:
            print(f"Error, Error due to {str(ep)}")
