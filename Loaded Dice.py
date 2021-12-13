#!/usr/bin/env python
# coding: utf-8

# In[10]:


import requests
from bs4 import BeautifulSoup
  
URL = "https://www.loadeddicebrewery.com/tap-list"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())


# In[15]:


imgs = soup.findAll("a", {"class": "p"})
print (imgs)


# In[55]:


import re
import requests
from bs4 import BeautifulSoup

site = 'https://www.loadeddicebrewery.com/tap-list'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img = soup.findAll('img')

ls=[]

for i in img:
    ls.append(img)


# In[45]:


print(img[4])


# In[57]:


print(ls)

