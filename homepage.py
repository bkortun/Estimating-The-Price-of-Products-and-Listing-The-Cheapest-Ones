# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 11:55:09 2022

@author: TULPAR
"""

from tkinter import *
from tkinter import ttk 
import pandas as pd
import numpy as np
import json
import random



fileObject = open("12_2022.json", "r")
jsonContent = fileObject.read()
dataList = json.loads(jsonContent)

productNames=["Domates","Salatalık","Peynir"]

master=Tk()

def onSearch():
    temp=-1  
    for i in range(1,4):
        
        rnd=random.randint(0,29)
        if(temp==rnd):
                rnd=random.randint(0,29)
       
        product_frame=Frame(master, bg="#D2C0BC")
        product_frame.place(relx=0.1,rely=0.21*i,relwidth=0.8,relheight=0.2)
        
        productName_label=Label(product_frame,text=dataList["Name"][str(rnd)],font="Verdana 12 bold",bg="#D2C0BC", anchor="w")
        productName_label.place(relx=0.2,rely=0.17,relwidth=0.62,relheight=0.2)
        
        productPrice_label=Label(product_frame,text=dataList["Price"][str(rnd)],font="Verdana 12 bold",bg="#D2C0BC", anchor="w")
        productPrice_label.place(relx=0.2,rely=0.55,relwidth=0.2,relheight=0.2)
        
        nextMonthPrice_label=Label(product_frame,text="Next Month Price: 111₺",font="Verdana 12 bold",bg="#D2C0BC", anchor="w")
        nextMonthPrice_label.place(relx=0.42,rely=0.55,relwidth=0.33,relheight=0.2)
        
        marketName_label=Label(product_frame,text=dataList["MarketName"][str(rnd)],font="Verdana 12 bold",bg="#D2C0BC")
        marketName_label.place(relx=0.79,rely=0.17,relwidth=0.18,relheight=0.58)
        
        seeDetails_button=Button(product_frame,text="See Details",font="Verdana 12 bold",command=lambda rnd=rnd:onClick(str(rnd)))
        seeDetails_button.place(relx=0.01,rely=0.17,relwidth=0.18,relheight=0.63)
        
        homepage_products.append(rnd)
        temp=rnd
    

canvas=Canvas(master,height=500,width=900,bg="#E2CFCB")
canvas.pack()

search_frame=Frame(master, bg="#E2CFCB")
search_frame.place(relx=0.1,rely=0.07,relwidth=0.8,relheight=0.1)

search_button=Button(search_frame,text="Search",font="Verdana 12 bold",command=onSearch)
search_button.place(relx=0.001,rely=0.17,relwidth=0.19,relheight=0.63)

search_text=Text(search_frame,height=10,width=75,font=("Verdana 12 bold",14))
search_text.place(relx=0.2,rely=0.17,relwidth=0.8,relheight=0.63)


def onClick(id):
    detail=Tk()
    
    canvasDetail=Canvas(detail,height=500,width=900,bg="#E2CFCB")
    canvasDetail.pack()
    
    product_frame=Frame(detail, bg="#D2C0BC")
    product_frame.place(relx=0.1,rely=0.21*i,relwidth=0.8,relheight=0.2)
    
    productName_label=Label(product_frame,text=dataList["Name"][id],font="Verdana 12 bold",bg="#D2C0BC", anchor="w")
    productName_label.place(relx=0.2,rely=0.17,relwidth=0.62,relheight=0.2)
    
    productPrice_label=Label(product_frame,text=dataList["Price"][id],font="Verdana 12 bold",bg="#D2C0BC", anchor="w")
    productPrice_label.place(relx=0.2,rely=0.55,relwidth=0.2,relheight=0.2)
    
    nextMonthPrice_label=Label(product_frame,text="Next Month Price: 111₺",font="Verdana 12 bold",bg="#D2C0BC", anchor="w")
    nextMonthPrice_label.place(relx=0.42,rely=0.55,relwidth=0.33,relheight=0.2)
    
    marketName_label=Label(product_frame,text=dataList["MarketName"][id],font="Verdana 12 bold",bg="#D2C0BC")
    marketName_label.place(relx=0.79,rely=0.17,relwidth=0.18,relheight=0.58)
    
    redirect_button=Button(product_frame,text="go to web site",font="Verdana 12 bold")
    redirect_button.place(relx=0.01,rely=0.17,relwidth=0.18,relheight=0.63)
    
    detail.mainloop()
    
    
temp=-1  
homepage_products=[]
list_frame=Frame(master,bg="black")
list_frame.place(relx=0.1,rely=0.21,relwidth=0.8,relheight=0.6)
  
for i in range(1,4):
    
    rnd=random.randint(0,29)
    if(temp==rnd):
            rnd=random.randint(0,29)
   
    product_frame=Frame(master, bg="#D2C0BC")
    product_frame.place(relx=0.1,rely=0.21*i,relwidth=0.8,relheight=0.2)
    
    productName_label=Label(product_frame,text=dataList["Name"][str(rnd)],font="Verdana 12 bold",bg="#D2C0BC", anchor="w")
    productName_label.place(relx=0.2,rely=0.17,relwidth=0.62,relheight=0.2)
    
    productPrice_label=Label(product_frame,text=dataList["Price"][str(rnd)],font="Verdana 12 bold",bg="#D2C0BC", anchor="w")
    productPrice_label.place(relx=0.2,rely=0.55,relwidth=0.2,relheight=0.2)
    
    nextMonthPrice_label=Label(product_frame,text="Next Month Price: 111₺",font="Verdana 12 bold",bg="#D2C0BC", anchor="w")
    nextMonthPrice_label.place(relx=0.42,rely=0.55,relwidth=0.33,relheight=0.2)
    
    marketName_label=Label(product_frame,text=dataList["MarketName"][str(rnd)],font="Verdana 12 bold",bg="#D2C0BC")
    marketName_label.place(relx=0.79,rely=0.17,relwidth=0.18,relheight=0.58)
    
    seeDetails_button=Button(product_frame,text="See Details",font="Verdana 12 bold",command=lambda rnd=rnd:onClick(str(rnd)))
    seeDetails_button.place(relx=0.01,rely=0.17,relwidth=0.18,relheight=0.63)
    
    homepage_products.append(rnd)
    temp=rnd
    


master.mainloop()




