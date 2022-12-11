# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 19:23:12 2022

@author: TULPAR
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime
import json

timeNow = datetime.datetime.now()
baseUrl="https://www.sokmarket.com.tr/"
productName=[]
productPrice=[]
productLink=[]
r_list=[]

r=requests.get("https://www.sokmarket.com.tr/domates-kg-p-6049/")
print(r.text)

soup=BeautifulSoup(r.content,"html.parser")

product=soup.find("div",{"class":"highlight-info"})
print(product)
#product_href=product.find('a')['href']
#product_list=[x.get_text().split("\n") for x in product]