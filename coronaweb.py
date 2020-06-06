# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 21:39:10 2020

@author: viswa janith
"""

import requests
import tkinter as tk
import bs4
import time
import plyer
import threading

def get_html_url(url):
    data=requests.get(url)
    return data

def corona_india():
    url="https://www.mohfw.gov.in/"
    html_data=get_html_url(url)
    bs=bs4.BeautifulSoup(html_data.text,'html.parser')
    info_div=bs.find("div",class_="site-stats-count").find_all("div",class_="iblock")
    all_details=""
    for block in info_div:
         count=block.find("span",class_="icount").get_text()
         text=block.find("div",class_="info_label").get_text()
         all_details=all_details + text +":"+ count
    return all_details

    
def refresh():
    newdata=corona_india()
    mainlabel['text']=newdata
    
#notify me
def notify_me():
    while True:
        plyer.notification.notify(
                title="COVID 20 cases of INDIA",
                message=corona_india(),
                timeout=10,
                app_icon='icon.ico'
                )
        time.sleep(30)
#creating GUI
root=tk.Tk()
root.geometry("900x800")
root.iconbitmao("icon.ico")
root.title("CORONA DATA TRACKER INDIA")
root.configure(background='white')
f=("poppins",25,"bold")

banner=tk.PhotoImage(file="banner.png")
bannerLabel=tk.Label(root,image=banner)
bannerLabel.pack()

mainlabel=tk.Label(root,text=corona_india(),font=f,bg='white')
mainlabel.pack()

rebtn=tk.button(root,text="REFRESH",font=f,releif='solid',command=refresh)
rebtn.pack()

th1=threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()

root.mainloop