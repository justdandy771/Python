# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 19:53:45 2020

@author: Ryan
"""


import urllib.request
import re
import pandas as pd
import sched, time
import smtplib
import email



scheduled_time = sched.scheduler(time.time, time.sleep)

def BeerScrape(sc):
    end=[]
    temp=[]
    x=0
    url='https://www.rakebeerproject.com/'
    response = urllib.request.urlopen(url).read()
    
    # Print the text inside an HTML element
    p = re.findall('{"products":((.|\s)+?){"products":', str(response)) 
    
    
    l=re.split((r'"'),str(p))
    
    for i in l:
       if l[x]=='name':
           temp=[l[x+2],l[x+6][0:10],l[x+6][11:]]
           end.append(temp)
           x+=1
       else:
           x+=1 
    
    df=pd.DataFrame(end)
    
    df.columns=['Beer Name','Date','Time Release']
    
    df['Date'] = df['Date'].astype('datetime64[ns]') 
    
    df=df.sort_values(by=['Date'],ascending=False)
    
    df=df.reset_index(drop=True, inplace=False)
    
    scheduled_time.enter(10, 1, BeerScrape, (sc,))
    
    print(df)
    
    """
    Section to send email and contents as a string dataframe to email
    """
    msg = email.message_from_string(df.to_string())
    msg['From'] = "ryan_foster771@hotmail.com"
    msg['To'] = "2315807229@vtext.com"
    msg['Subject'] = "Beer Update"
    
    s = smtplib.SMTP("smtp.live.com",587)
    s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
    s.starttls() #Puts connection to SMTP server in TLS mode
    s.ehlo()
    s.login('ryan_foster771@hotmail.com', 'Ibanez_970w')      
    s.sendmail("ryan_foster771@hotmail.com", "2315807229@vtext.com", msg.as_string()) # first email from second is the to
    
    s.quit()
"""
Time in seconds to sleep, number of cycles    
""" 
scheduled_time.enter(1, 1, BeerScrape, (scheduled_time,))
scheduled_time.run()



print(BeerScrape)

 
# export = df.to_csv(r'C:\Users\Ryan\Downloads\Beer.csv', index = None, header=True) 


