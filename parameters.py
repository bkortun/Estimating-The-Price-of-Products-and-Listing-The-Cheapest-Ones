# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 18:54:19 2022

@author: TULPAR
"""

import requests
from bs4 import BeautifulSoup
import os
import json
import pandas as pd
import datetime

url="https://www.bloomberght.com/"
response= requests.get(url)
timeNow = datetime.datetime.now()

HtmlContent=response.content
soup = BeautifulSoup(HtmlContent,"html.parser")

html=list()
html = soup.find_all("small",{"class":"value LastPrice"})


dataValues=list()
dataNames=list()
dateTime=list()


for i in html:
    dataValues.append(i.text)
    dataNames.append(i.get("data-secid"))
    dateTime=datetime.datetime.now()
    
    
dictionary={
    "DataNames":dataNames,
    "DataValues":dataValues,
    "time":dateTime
    }

parameters_df=pd.DataFrame(dictionary)
parameters_df.to_json(r''+format(timeNow.month)+"_"+format(timeNow.year)+'parameters.json')

if os.path.exists("parameters.json"):
    data_df=pd.read_json("parameters.json")
    parameters_df=pd.concat([data_df,parameters_df],axis=0)
    parameters_df.reset_index(drop=True,inplace=True)

parameters_df.to_json(r'parameters.json')

