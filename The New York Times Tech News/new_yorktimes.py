from bs4 import BeautifulSoup
import pandas as pd
from requests import get

df =  pd.read_csv('new_york_times_tech.csv')
headline = list()
date = list()
author = list()
description  = list()

for i in range(1,11):
    if i == 1:
        url = "https://www.nytimes.com/section/technology" 
    else:
        url = "https://www.nytimes.com/section/technology"+"?page="+str(i)

    page = get(url)
    soup  = BeautifulSoup(page.content,'html.parser')

    headlines = soup.select("h3.css-1kv6qi.e15t083i0")
    for j in headlines:
        headline.append(j.text)

    descriptions = soup.select("p.css-1pga48a.e15t083i1")
    for m in descriptions:
        description.append(m.text)
    

df['Headline'] = headline
df['Description'] = description

df.to_csv('new_york_times_tech.csv',index=False)

    
    

    