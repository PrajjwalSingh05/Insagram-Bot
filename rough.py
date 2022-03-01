from distutils import command

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("D:/Project/New folder/Instagram_Bot/Chromedriver.exe")

# driver=webdriver.Chrome("D:/Project/New folder/Instagram_Bot/Chromedriver.exe")
driver.get("https://www.instagram.com/")
print("inside driver")
try:
            user_name="tester05032002@gmail.com"
            user_password="9450752717"
            # user_name=username.get()
            # user_password=password.get()
            if user_name=="" or user_password=="":
                messagebox.showerror("Error","All Field required")
            else:
              
                user_path = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
                # user_path=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
                user_path.send_keys(user_name)
                password_path= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
                # password_path=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
                password_path.send_keys(user_password)
                # login_button=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
                login_button=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="loginForm"]/div/div[3]/button/div')))
                # login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]')))
                login_button.click()

                # not_now_option=driver.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button")
                not_now_option=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button')))
                not_now_option.click()
                time.sleep(5)
                # remember_me_option=driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
                remember_me_option=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')))
                remember_me_option.click()
                # time.sleep(5)
                

except Exception as ep:
            print(f"Error, Error due to {str(ep)}")

time.sleep(1)