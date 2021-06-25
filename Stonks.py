# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:27:31 2021

@author: ryan_
"""

import yfinance as yf
import datetime #for reading present date
import time 
import requests #for retreiving coronavirus data from web
from plyer import notification #for getting notification on your PC

def TRCH_ticker():
    ticker = yf.Ticker("TRCH")
    symbol=ticker.info['symbol']
    dailyhigh =ticker.info['regularMarketDayHigh']
    dailylow =ticker.info['regularMarketDayLow']
    dailyopen =ticker.info['previousClose']
    current=float(ticker.info['bid'])
    change=(float(current)-float(dailyopen))/(float(dailyopen))*100
    change=round(change,2)

    
    print(symbol, 'Daily High:', '$'+str(dailyhigh),'Daily Low:', '$'+str(dailylow),'Open:', '$'+str(dailyopen), 'Current Bid:', '$'+str(current), 'Change:', str(change)+'%')



# def notifyMe(ticker,current):
#     notification.notify(
#         ticker = ticker,
#         current = current,
#         app_icon = r"C:\Users\ryan_\Documents\Python Scripts\Python\Tribalmarkings-Aquave-Cash-Dollar-folder.ico", #http://www.iconarchive.com/show/qetto-2-icons-by-ampeross/timer-icon.html
#         timeout = 1,    )
    
TRCH_ticker()

