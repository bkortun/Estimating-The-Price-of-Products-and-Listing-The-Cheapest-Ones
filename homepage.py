# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 11:55:09 2022

@author: TULPAR
"""

""


from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import pandas as pd
import numpy as np
import json
import random
import os
import datetime


timeNow = datetime.datetime.now()

if os.path.exists(format(timeNow.month)+"_"+format(timeNow.year)+'.json')==False:
        os.system('python webScrapper.py')
        os.system('python parameters.py')

fileObject = open(format(timeNow.month)+"_"+format(timeNow.year)+'.json', "r")        
jsonContent = fileObject.read()
dataList = json.loads(jsonContent)



productNames=dataList["Name"]
productPrices=dataList["Price"]

names=list(productNames.values())
prices=list(productPrices.values())
master=Tk()

products=[]

def onSearch(input):
    if input=="":
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
        
            temp=rnd
    else:
        products=[]
        sortedProducts=[]
        selectedIndexes=[]
        sortedUtils=[0,1,2]
        index=0
        for item in names:
            if input.lower() in item.lower():
                    products.append(index)
                    sortedProducts.append(prices[index])
                    selectedIndexes=np.argsort(sortedProducts)
                    
                    if len(selectedIndexes)==3:
                        for i in range(0,3):
                            if selectedIndexes[i]==0:
                                    sortedUtils[0]=products[i]
                            if selectedIndexes[i]==1:
                                    sortedUtils[1]=products[i]
                            if selectedIndexes[i]==2:
                                    sortedUtils[2]=products[i]
                    sortedProducts.sort()
                    
            index=index+1
        if len(sortedProducts)==0:
            messagebox.showerror("Attention", "The product with the name you entered was not found!")
        else:
            for i in range(1,4):
                
                
                           
                product_frame=Frame(master, bg="#D2C0BC")
                product_frame.place(relx=0.1,rely=0.21*i,relwidth=0.8,relheight=0.2)
                
                productName_label=Label(product_frame,text=dataList["Name"][str(sortedUtils[i-1])],font="Verdana 12 bold",bg="#D2C0BC", anchor="w")
                productName_label.place(relx=0.2,rely=0.17,relwidth=0.62,relheight=0.2)
                
                productPrice_label=Label(product_frame,text=sortedProducts[i-1],font="Verdana 12 bold",bg="#D2C0BC", anchor="w")
                productPrice_label.place(relx=0.2,rely=0.55,relwidth=0.2,relheight=0.2)
                
                nextMonthPrice_label=Label(product_frame,text="Next Month Price: 111₺",font="Verdana 12 bold",bg="#D2C0BC", anchor="w")
                nextMonthPrice_label.place(relx=0.42,rely=0.55,relwidth=0.33,relheight=0.2)
                
                marketName_label=Label(product_frame,text=dataList["MarketName"][str(sortedUtils[i-1])],font="Verdana 12 bold",bg="#D2C0BC")
                marketName_label.place(relx=0.79,rely=0.17,relwidth=0.18,relheight=0.58)
                
                seeDetails_button=Button(product_frame,text="See Details",font="Verdana 12 bold",command=lambda i=i:onClick(str(products[i-1])))
                seeDetails_button.place(relx=0.01,rely=0.17,relwidth=0.18,relheight=0.63)
            input=""
            index=0
        


canvas=Canvas(master,height=500,width=900,bg="#E2CFCB")
canvas.pack()

search_frame=Frame(master, bg="#E2CFCB")
search_frame.place(relx=0.1,rely=0.07,relwidth=0.8,relheight=0.1)

search_button=Button(search_frame,text="Search",font="Verdana 12 bold",command=lambda :onSearch(search_text.get("1.0",'end-1c')))
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
    
    
    detail.mainloop()
    
    

temp=-1  
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
    
    temp=rnd
    
    
webScrapping_button=Button(master,text="Web Scrapping",font="Verdana 12 bold",command=lambda :os.system('python webScrapper.py'))
webScrapping_button.place(relx=0.05,rely=0.88,relwidth=0.15,relheight=0.1)

parameters_button=Button(master,text="Parameters",font="Verdana 12 bold",command=lambda :os.system('python parameters.py'))
parameters_button.place(relx=0.25,rely=0.88,relwidth=0.15,relheight=0.1)

master.mainloop()





