# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:56:24 2022

@author: TULPAR
"""

from bs4 import BeautifulSoup
import requests
import json
import os
import pandas as pd
import datetime

timeNow = datetime.datetime.now()
baseUrl="https://www.a101.com.tr"
productName=[]
productPrice=[]
productLink=[]
marketName=[]
r_list=[]

#Webpage Adresses
r_domates=requests.get("https://www.a101.com.tr/list/?search_text=domates&personaclick_search_query=domates&personaclick_input_query=domates")
r_salatalik=requests.get("https://www.a101.com.tr/list/?search_text=salatal%C4%B1k&personaclick_search_query=salatal%C4%B1k&personaclick_input_query=salatal%C4%B1k")
r_peynir=requests.get("https://www.a101.com.tr/list/?search_text=peynes%20peynir&personaclick_search_query=peynes%20peynir&personaclick_input_query=peynes%20peynir")
r_zeytin=requests.get("https://www.a101.com.tr/list/?search_text=Zeo%20Siyah%20Zeytin%20Xs-2xs%20500%20G&personaclick_search_query=Zeo%20Siyah%20Zeytin%20Xs-2xs%20500%20G&personaclick_input_query=Zeo%20Siyah%20Zeytin%20Xs-2xs%20500%20G")
r_sucuk=requests.get("https://www.a101.com.tr/list/?search_text=Torku%20Dana%20Kangal%20Fermente%20Sucuk%20350%20g&personaclick_search_query=Torku%20Dana%20Kangal%20Fermente%20Sucuk%20350%20g&personaclick_input_query=Torku%20Dana%20Kangal%20Fermente%20Sucuk%20350%20g")
r_mayonez=requests.get("https://www.a101.com.tr/list/?search_text=Burcu%20Mayonez%20550%20G&personaclick_search_query=Burcu%20Mayonez%20550%20G&personaclick_input_query=Burcu%20Mayonez%20550%20G")
r_camasir=requests.get("https://www.a101.com.tr/list/?search_text=%C3%A7ama%C5%9F%C4%B1r%20deterjan&personaclick_search_query=%C3%A7ama%C5%9F%C4%B1r%20deterjan&personaclick_input_query=%C3%A7ama%C5%9F%C4%B1r%20deterjan")
r_yag=requests.get("https://www.a101.com.tr/list/?search_text=yag&personaclick_search_query=yag&personaclick_input_query=yag")
r_kakao=requests.get("https://www.a101.com.tr/list/?search_text=Findux%20Kakaolu%20F%C4%B1nd%C4%B1k%20Kremas%C4%B1%20400%20G&personaclick_search_query=Findux%20Kakaolu%20F%C4%B1nd%C4%B1k%20Kremas%C4%B1%20400%20G&personaclick_input_query=Findux%20Kakaolu%20F%C4%B1nd%C4%B1k%20Kremas%C4%B1%20400%20G")
r_bulasik=requests.get("https://www.a101.com.tr/list/?search_text=Miss%20Bula%C5%9F%C4%B1k%20Deterjan%C4%B1%201%20L&personaclick_search_query=Miss%20Bula%C5%9F%C4%B1k%20Deterjan%C4%B1%201%20L&personaclick_input_query=Miss%20Bula%C5%9F%C4%B1k%20Deterjan%C4%B1%201%20L")

r_list.append(r_domates)
r_list.append(r_salatalik)
r_list.append(r_peynir)
r_list.append(r_zeytin)
r_list.append(r_sucuk)
r_list.append(r_mayonez)
r_list.append(r_camasir)
r_list.append(r_yag)
r_list.append(r_kakao)
r_list.append(r_bulasik)

#Arrange Source Code
for r in r_list:        
    soup=BeautifulSoup(r.content,"html.parser")
        
    product=soup.find("article",{"class":"product-card"})
    product_href=product.find('a')['href']
    product_list=[x.get_text().split("\n") for x in product]
    for product in product_list:
        if(product==product_list[1]):
            productName.append(product[5].strip()) 
            essantial=product[10].split("₺")
            productPrice.append(essantial[1]) 
            productLink.append(baseUrl+product_href)
            marketName.append("A-101")
    product_list=[]



        

baseUrl="https://www.carrefoursa.com"
r_list=[]

r_domates=requests.get("https://www.carrefoursa.com/search/?text=domates")
r_salatalik=requests.get("https://www.carrefoursa.com/search/?text=salatal%C4%B1k")
r_peynir=requests.get("https://www.carrefoursa.com/search/?text=Carrefour+S%C3%BCzme+Peynir+1000+g")
r_zeytin=requests.get("https://www.carrefoursa.com/search/?text=siyah+zeytin+500")
r_sucuk=requests.get("https://www.carrefoursa.com/search/?text=P%C4%B1nar+Sucuk+Mangal+Keyfi+300+g")
r_mayonez=requests.get("https://www.carrefoursa.com/search/?text=Tat+Mayonez+550+g")
r_camasir=requests.get("https://www.carrefoursa.com/search/?text=Perwoll+Hassas+S%C4%B1v%C4%B1+%C3%87ama%C5%9F%C4%B1r+Deterjan%C4%B1+Renkli+3+L")
r_yag=requests.get("https://www.carrefoursa.com/search/?text=ay%C3%A7i%C3%A7ek+ya%C4%9F%C4%B1")
r_kakao=requests.get("https://www.carrefoursa.com/search/?text=Carrefour+Kakaolu+F%C4%B1nd%C4%B1k+Kremas%C4%B1+400+g")
r_bulasik=requests.get("https://www.carrefoursa.com/search/?text=Carrefour+Limon+Kokulu+Bula%C5%9F%C4%B1k+Deterjan%C4%B1+750+ml")

r_list.append(r_domates)
r_list.append(r_salatalik)
r_list.append(r_peynir)
r_list.append(r_zeytin)
r_list.append(r_sucuk)
r_list.append(r_mayonez)
r_list.append(r_camasir)
r_list.append(r_yag)
r_list.append(r_kakao)
r_list.append(r_bulasik)

for r in r_list:
    soup=BeautifulSoup(r.content,"html.parser")
    product=soup.find("li",{"class":"product-listing-item"})
    product_href=product.find('a')['href']
    product_list=[x.get_text().split("\n") for x in product]

    for product in product_list:
           if(len(product)>20):
               productName.append(product[15].strip()) 
               if(product[19]==''):
                   essantial=product[21].split()
                   productPrice.append(essantial[0]) 
               else:
                   essantial=product[19].split()
                   productPrice.append(essantial[0]) 
               productLink.append(baseUrl+product_href)
               marketName.append("Carrefoursa")
               

               
baseUrl="https://tahtakalespot.com"
r_list=[]

r_domates=requests.get("https://tahtakalespot.com/search/mevsiminden%20domates/5991f7c3-7305-4717-9c26-bcf5fbc8e491")
r_salatalik=requests.get("https://tahtakalespot.com/search/mevsiminden%20salatal%C4%B1k/d80f3186-fea0-418b-b12b-292078a4e7a7")
r_peynir=requests.get("https://tahtakalespot.com/search/S%C3%BCta%C5%9F%20S%C3%BCzme%20Beyaz%20Peynir%201000gr/5bd4dcea-5e06-4b38-9a24-3a4cd88ab2d9")
r_zeytin=requests.get("https://tahtakalespot.com/search/Mevsiminden%20Kuru%20Sele%20Zeytin%20%28kg%29%28291-320%29/676b5370-cea6-4658-a97f-36627475e1b2")
r_sucuk=requests.get("https://tahtakalespot.com/search/%C4%B0kbal%20Dana%20Kangal%20Sucuk%20200gr/b1ce7f0b-3e83-41e0-b595-f77005850668")
r_mayonez=requests.get("https://tahtakalespot.com/search/mayonez/dbabc6f5-b1a5-4724-aa31-296825522067")
r_camasir=requests.get("https://tahtakalespot.com/search/Bingo%20S%C4%B1v%C4%B1%20%C3%87ama%C5%9F%C4%B1r%20Renki%20Beyaz%202145Ml%2033%20Y%C4%B1kama/9a40d861-0cea-4c5d-9955-f8c181be66fb")
r_yag=requests.get("https://tahtakalespot.com/search/Oru%C3%A7o%C4%9Flu%20Ay%C3%A7i%C3%A7ek%20Ya%C4%9F%C4%B1%201lt%20Pet/5a239557-911f-4cef-8211-fecfcaa68ddf")
r_kakao=requests.get("https://tahtakalespot.com/search/SARELLE%20KAKAOLU%20FINDIK%20KREMASI%20350gr/707a60f0-eede-4013-b662-6af743af36dd")
r_bulasik=requests.get("https://tahtakalespot.com/search/bula%C5%9F%C4%B1k%20deterjan%C4%B1/e260680d-a246-432e-b443-1f1174aa4ca2")

r_list.append(r_domates)
r_list.append(r_salatalik)
r_list.append(r_peynir)
r_list.append(r_zeytin)
r_list.append(r_sucuk)
r_list.append(r_mayonez)
r_list.append(r_camasir)
r_list.append(r_yag)
r_list.append(r_kakao)
r_list.append(r_bulasik)
             
for r in r_list:
    soup=BeautifulSoup(r.content,"html.parser")
    product=soup.find("div",{"class":"product bordered"})
    product_href=product.find('a')['href']
    product_list=[x.get_text().split("\n") for x in product]
    productName.append(product_list[4][0]) 
    productPrice.append(product_list[7][0].split()[0]) 
    productLink.append(baseUrl+product_href)
    marketName.append("Tahtakale")
              
        
#Table Writing Process
product_dict={"Name":productName,"Price":productPrice,"Time":timeNow,"Link":productLink,"MarketName":marketName}
product_df=pd.DataFrame(product_dict)
product_df.to_json(r''+format(timeNow.month)+"_"+format(timeNow.year)+'.json')

if os.path.exists("data.json"):
    data_df=pd.read_json("data.json")
    product_df=pd.concat([data_df,product_df],axis=0)
    product_df.reset_index(drop=True,inplace=True)

product_df.to_json(r'data.json')




