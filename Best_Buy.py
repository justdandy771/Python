# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:47:22 2021

@author: ryan_
"""


import requests
from bs4 import BeautifulSoup
import smtplib
import sched, time

global url

scheduled_time = sched.scheduler(time.time, time.sleep)

from_email="ryan_foster771@hotmail.com"
to_email="2315807229@vtext.com"
email_subject="GPU In Stock"
username="ryan_foster771@hotmail.com"
password='Ibanez_970w'

timing='Attempt'
x=1

def send_email(url):
      
    #Create Headers
    headers = ["From: " + from_email, "Subject: " + email_subject, "To: " + to_email,
               "MIME-Version: 1.0", "Content-Type: text/html"]
    headers = "\r\n".join(headers)
  
    #Connect to Gmail Server
    session = smtplib.SMTP("smtp.live.com",587)
    session.ehlo()
    session.starttls()
    session.ehlo()
  
    #Login to Gmail
    session.login(username, password)
  
    #Send Email & Exit
    session.sendmail(from_email, to_email, headers + "\r\n\r\n" + url)
    session.quit
  

 


#Spoofing the user agent request
def get_page_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    return page.content

#Loading parser and the scraping agent
def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_div = soup.find("button", {"class": "btn btn-disabled btn-lg btn-block add-to-cart-button"})
    return out_of_stock_div == "Sold Out"

#Checking the cards
def check_XFX_Reference_RX6800xt():
    global url
    url = "https://www.bestbuy.com/site/xfx-amd-radeon-rx-6800xt-16gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6441226.p?skuId=6441226"
    page_html = get_page_html(url)
    if check_item_in_stock(page_html):
        send_email(url)
    else:
        pass
    
def check_Asus_Strix_3080():
    global url
    url = "https://www.bestbuy.com/site/asus-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-strix-graphics-card-black/6432445.p?skuId=6432445"
    page_html = get_page_html(url)
    if check_item_in_stock(page_html):
        send_email(url)
    else:
        pass
    
def check_NVIDIA_Reference_3080():
    global url
    url = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
    page_html = get_page_html(url)    
    if check_item_in_stock(page_html):
        send_email(url)
    else:
        pass

def check_Gigabyte_3080():
    global url
    url = "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3080-aorus-master-10gb-rev-2-0-gddr6x-pci-express-4-0-graphics-card/6462198.p?skuId=6462198"
    page_html = get_page_html(url)    
    if check_item_in_stock(page_html):
        send_email(url)
    else:
        pass

def check_Gigabyte_Aorus_3080():
    global url
    url = "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3080-aorus-master-10gb-gddr6x-pci-express-4-0-graphics-card/6436223.p?skuId=6436223"
    page_html = get_page_html(url)    
    if check_item_in_stock(page_html):
        send_email(url)
    else:
        pass

def check_Gigabyte_Eagle_3080():
    global url
    url = "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3080-eagle-oc-10gb-gddr6x-pci-express-4-0-graphics-card/6430621.p?skuId=6430621"
    page_html = get_page_html(url)    
    if check_item_in_stock(page_html):
        send_email(url)
    else:
        pass

def check_Gigabyte_Vision_3080():
    global url
    url = "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3080-vision-oc-10gb-gddr6x-pci-express-4-0-graphics-card/6436219.p?skuId=6436219"
    page_html = get_page_html(url)    
    if check_item_in_stock(page_html):
        send_email(url)
    else:
        pass

def check_NVIDIA_Reference_3090():
    global url
    url = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434"
    page_html = get_page_html(url)    
    if check_item_in_stock(page_html):
        send_email(url)
    else:
        pass
    
def batch():
    check_XFX_Reference_RX6800xt()
    check_Asus_Strix_3080()
    check_NVIDIA_Reference_3080() 
    check_Gigabyte_3080()
    check_Gigabyte_Aorus_3080()
    check_Gigabyte_Eagle_3080()
    check_Gigabyte_Vision_3080()
    check_NVIDIA_Reference_3090()


while True: 
    batch()
    print(timing, x)
    x+=1
    time.sleep(30)
    





