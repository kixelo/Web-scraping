#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

wiki_url="https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
    
response=requests.get(wiki_url)
soup=BeautifulSoup(response.text,"html.parser")
 
table=soup.find("table", {"class":"wikitable sortable static-row-numbers plainrowheaders srn-white-background"}).tbody
 
rows=table.find_all("tr")
#print(rows)
columns=[v.text.replace("\n","").replace("[4]","") for v in rows[0].find_all("th")]

df = pd.DataFrame(columns = columns)

for i in range(1, len(rows)):
    tds = rows[i].find_all("td")
    #print(len(tds))
    
    if len(tds) == 7:
        values = [tds[0].text, tds[1].text.replace("\xa0","").replace("\n",""), tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text.replace("\xa0","").replace("\n","")]
    else:
        values = [td.text.replace("\xa0","").replace("\n","") for td in tds]
    
    df = df.append(pd.Series(values, index=columns, dtype='object'), ignore_index=True)
    print(df)
    
    


# In[7]:


df.to_csv("WikiScraping.csv")

