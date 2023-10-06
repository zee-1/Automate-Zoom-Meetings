
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

import time
Name = "GOD"                        #Place your name here
Roll_Num = "202259"
                #Place you roll number or anyhting you uuse for marking attendance
meets = ["https://us04web.zoom.us/j/73396851919?pwd=zVblWoH2Xe3o8QlapwdEVCWpRtlxZH.1"]           #Add classs link here "URL1","URL2"...so on
timings = ["08:42"]                                                                             #Add timing here in 24hr format "8:00","12:00"... so on
map_meet = dict()
for i in range(len(meets)):
      map_meet[timings[i]]=meets[i]

options = Options()
options.set_preference("media.navigator.permission.disabled", False)

def JoinMeet(URL):
      browse = webdriver.Firefox()
      browse.implicitly_wait(30)
      browse.get(URL)
      time.sleep(10)
      butt = browse.find_element_by_xpath("//div[contains(@class, 'mbTuDeF1')]")
      butt.click()
      time.sleep(3)
      buttt=browse.find_element_by_link_text("Join from Your Browser")
      buttt.click()
      time.sleep(3)
      bu = browse.find_element_by_id("inputname")
      bu.send_keys(Name)
      join = browse.find_element_by_xpath("//*[@id="+"\"join-form-container\""+"]/div[4]/div").click()
      Join_audio = WebDriverWait(browse, 1000000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div/div[2]/div[3]/div/div[2]/div/button'))).click()
      mute = WebDriverWait(browse, 1000000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div/div/div/footer/div/div[1]/div[1]/button'))).click()
      open_chat = WebDriverWait(browse, 1000000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div/div/div/footer/div/div[2]/div[3]/button'))).click()
      _send_atten = WebDriverWait(browse, 1000000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div/div/div[2]/div/div[4]/textarea')))
      send_atten = browse.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[3]/div/div/div[2]/div/div[4]/textarea")
      send_atten.send_keys(Roll_Num+" present")             #"The text to be written in text box as attnedance"
      send_atten.send_keys(Keys.RETURN)
      time.sleep(40*60)
      browse.quit()
 
while True:
      if (len(timings)!=len(meets)):
            print("Aborting count of Timings is not equal to count of meets")
      else:
            #print(datetime.now().strftime("%H:%M"))
            if datetime.now().strftime("%H:%M") in timings:
                  print("You Have a meeting")
                  JoinMeet(map_meet[datetime.now().strftime("%H:%M")])
