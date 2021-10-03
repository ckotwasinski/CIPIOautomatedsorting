#!/usr/bin/env python
# coding: utf-8

# In[263]:


import pandas as pd
import numpy as np
import re
import datefinder
from datetime import datetime, timedelta 
import json


# In[264]:



def read_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


# In[ ]:





# In[265]:


def createDictionary():    
    dataDict = {}

    keyList = ["email","gender","dob","firstName","lastName","state","city","zipcode","address","customer_status","mem_status","pkg_interval_count","dob","join_date","mem_start_date","mem_end_date","mobile_phone","total_price","payment_provider","mem_type","pkg_name","mem_id","pkg_id","plan_name","currency","item_info","title","duration","period_start","period_end","payment_paid_date","video_published_date"]

    for i in keyList:
        dataDict[i] = []
    
    return dataDict


# In[ ]:





# In[266]:


def findFullrow(df):
    fullrow = []
    fullrowAddy = []
    for i in range(len(df.columns)):
        for j in range(int(int(df.size)/len(df.columns))):
            data = df.loc[j, df.columns[i]]
            if str(data) != "nan":
                fullrow.append(data)
                fullrowAddy.append((j, df.columns[i]))
                break
            if j == int(int(df.size)/len(df.columns)):
                print(df.size)
                print(j)
                fullrowAddy.append((j, df.columns[i]))
                fullrow.append(None)
    return fullrow, fullrowAddy


# In[267]:


def searchRow(df, fullrow, fullrowAddy):
    for i in range(len(fullrow)):
        fullrow[i] = df.loc[fullrowAddy[i][0]+1,fullrowAddy[i][1]]
        temp = list(fullrowAddy[i])
        temp[0] = temp[0]+1
        fullrowAddy[i] = tuple([temp[0], fullrowAddy[i][1]]) 
    return fullrow, fullrowAddy


# In[ ]:





# In[268]:


def phoneNumber(item):
    if type(item) == str:
        match = re.search(r'(\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4})', item)
        if match != None:
            return True
    return False


# In[269]:


def findName(column, config):
    if type(column)==str:
        if "name" in column or "Name" in column:
            searches = config["SEARCH_TERMS"]["name"]
            for search in searches:
                if search in column:
                    return True
    return False


# In[270]:


def findEmail(item):
    if type(item)==str:
        match = re.search(r'[\w\.-]+@[\w\.-]+', item)
        if match != None:
            return True
    return False


# In[271]:


def findState(column, config):
    if type(column)== str:
        searches = config["SEARCH_TERMS"]["state"]
        for search in searches:
            if search in column:
                return True
    return False


# In[272]:


def findCity(column,config):
    if type(column)== str:
        searches = config["SEARCH_TERMS"]["city"]
        for search in searches:
            if search in column:
                return True
    return False


# In[273]:


def findZip(column, config):
    if type(column)== str:
        searches = config["SEARCH_TERMS"]["zip"]
        for search in searches:
            if search in column:
                return True
    return False


# In[274]:


def findAddress(column,config):
    if type(column)== str:
        searches = config["SEARCH_TERMS"]["address"]
        for search in searches:
            if search in column:
                return True
    return False


# In[275]:


def findGender(item,config):
    if type(item)== str:
        searches = config["SEARCH_TERMS"]["gender"]
        for search in searches:
            if search in item:
                return True
    return False


# In[276]:


def findContractState(column,config):
    if type(column)== str:
        searches = config["SEARCH_TERMS"]["contractState"]
        for search in searches:
            if search in column:
                return True
    return False


# In[277]:


def findMembershipType(item,config):
    if type(item)== str:
        searches = config["SEARCH_TERMS"]["interval"]
        for search in searches:
            if search in item:
                return True
    return False


# In[278]:


def findAgreement(column, config):
    if type(column)== str:
        searches = config["SEARCH_TERMS"]["agreement"]
        for search in searches:
            if search in column:
                return True
    return False


# In[279]:


def findProductName(column,config):
    if type(column) == str:
        if 'name' in column or 'Name' in column or 'offer' in column or 'Offer' in column:
            searches = config["SEARCH_TERMS"]["productName"]
            for search in searches:
                if search in column:
                    return True
    return False


# In[280]:


def findMemberNumber(column,config):
    if type(column) == str:
        if 'id' in column or 'ID' in column or 'Id' in column:
            searches = config["SEARCH_TERMS"]["memberNumber"]
            for search in searches:
                if search in column:
                    return True
    return False


# In[281]:


def findCurrency(column,config):
    if type(column) == str:
        searches = config["SEARCH_TERMS"]["currency"]
        for search in searches:
                if search in column:
                    return True
    return False


# In[282]:


def findProductId(column,config):
    if type(column) == str:
        searches = ['id','ID','info','Info','name','Name']
        secondSearches = config["SEARCH_TERMS"]["productId"]
        for search in searches:
            if search in column:
                for secondSearch in secondSearches:
                    if secondSearch in column:
                        return True
    return False


# In[283]:


def findTitle(column,config):
    if type(column) == str:
        searches = config["SEARCH_TERMS"]["title"]
        for search in searches:
                if search in column:
                    return True
    return False


# In[284]:


def findDuration(column,config):
    if type(column) == str:
        searches = config["SEARCH_TERMS"]["duration"]
        for search in searches:
                if search in column:
                    return True
    return False


# In[285]:



def findDates(df, fullrow):
    dates=[]
    dateIndex = []
    for i in range(len(fullrow)):
        if type(fullrow[i])==str:
            matches = datefinder.find_dates(fullrow[i])
            for match in matches:
                dates.append(match)  
                dateIndex.append(df.columns[i])
    dates.sort()
    return dates, dateIndex


# In[286]:


def findPaymentSource(item,config):
    if type(item)== str:
        searches = config["SEARCH_TERMS"]["paymentSource"]
        for search in searches:
            if search in item:
                return True
    return False


# In[287]:


def findStartDates(column,config):
    if type(column) == str:
        if 'date' in column or 'Date' in column:
            searches = config["SEARCH_TERMS"]["startDates"]
            for search in searches:
                if search in column:
                    return True
    return False


# In[288]:


def findEndDates(column,config):
    if type(column) == str:
        if 'date' in column or 'Date' in column:
            searches = config["SEARCH_TERMS"]["endDates"]
            for search in searches:
                if search in column:
                    return True
    return False


# In[289]:


def findPaidDates(column,config):
    if type(column) == str:
        if 'date' in column or 'Date' in column:
            searches = config["SEARCH_TERMS"]["paidDates"]
            for search in searches:
                if search in column:
                    return True
    return False


# In[290]:


def findPublishDates(column,config):
    if type(column) == str:
        if 'date' in column or 'Date' in column:
            searches = config["SEARCH_TERMS"]["publishDates"]
            for search in searches:
                if search in column:
                    return True
    return False


# In[291]:


def findDob(dates, dateIndex):
    if len(dates) >= 2:
        if timedelta(days = 3650) > dates[1] - dates[0]:
            return False
        else:
            return True
    return False


# In[292]:


def checkColumns(df, dataDict,config):
    
    for column in df.columns:
        if config["DESTINATIONS"]["customer_profile"]:
            if findName(column,config):
                dataDict['firstName'].append(column)
                dataDict['lastName'].append(column)
            if findState(column,config):
                dataDict['state'].append(column)
            if findCity(column,config):
                dataDict['city'].append(column)
            if findZip(column,config):
                dataDict['zipcode'].append(column)
            if findAddress(column,config):
                dataDict['address'].append(column)
            if findContractState(column,config):
                dataDict['customer_status'].append(column)
            if findStartDates(column,config):
                dataDict['join_date'].append(column)
                dataDict['mem_start_date'].append(column)
                dataDict['period_start'].append(column)
            if findEndDates(column,config):
                dataDict['mem_end_date'].append(column)
                dataDict['period_end'].append(column)
            if findPaidDates(column,config):
                dataDict['mem_end_date'].append(column)
        if config["DESTINATIONS"]["membership"]:
            if findAgreement(column,config):
                dataDict['mem_type'].append(column)
            if findProductName(column,config):
                dataDict['plan_name'].append(column)
            if findMemberNumber(column,config):
                dataDict['mem_id'].append(column)
            if findProductId(column,config):
                dataDict['item_info'].append(column)
        if config["DESTINATIONS"]["membership_revenue"]:
            if findCurrency(column,config):
                dataDict['currency'].append(column)
        if config["DESTINATIONS"]["customer_attendance"]:
            if findTitle(column,config):
                dataDict['title'].append(column)
            if findDuration(column,config):
                dataDict['duration'].append(column)
            if findPublishDates(column,config):
                dataDict['video_published_date'].append(column)
        


# In[293]:


def checkRow(df, fullrow, dataDict,config):
    index = 0 
    dates, dateIndex = findDates(df, fullrow)
    for item in fullrow:
        if config["DESTINATIONS"]["customer_profile"]:
            if findEmail(item):
                dataDict['email'].append(df.columns[index])
            if phoneNumber(item):
                dataDict['mobile_phone'].append(df.columns[index])
            if findGender(item,config):
                dataDict['gender'].append(df.columns[index])
            if findDob(dates,dateIndex):
                dataDict['dob'].append(dateIndex[0])
        if config["DESTINATIONS"]["membership"]:
            if findMembershipType(item,config):
                dataDict['pkg_interval_count'].append(df.columns[index])
        if config["DESTINATIONS"]["membership_revenue"]:
            if findPaymentSource(item,config):
                dataDict['payment_provider'].append(df.columns[index])
        index = index + 1


# In[303]:


def searchAllRows(df,fullrow, fullrowAddy, dataDict, config):
    complete = {"paymentSource": False}
    for row in range(int(int(df.size)/len(df.columns))):
        index = 0
        fullrow, fullrowAddy = searchRow(df, fullrow, fullrowAddy)
        for item in fullrow:
            if config["DESTINATIONS"]["membership_revenue"]:
                if findPaymentSource(item,config):
                    dataDict['payment_provider'].append(df.columns[index]) 
                    complete["paymentSource"] = True
            if all(complete):
                return
            index = index + 1
            
        
    


# In[304]:


def arraytoString(array):
    newString = ""
    for item in array:
        newString = newString + " " + str(item)
    return newString


# In[305]:


def builddf():
    config = read_json("config.json")
    df = pd.read_csv(config["PROGRAM"]["INPUTFILE"])
    fullrow, fullrowAddy = findFullrow(df)
    dataDict = createDictionary()
    checkColumns(df, dataDict,config)
    checkRow(df, fullrow, dataDict,config)
    searchAllRows(df,fullrow, fullrowAddy, dataDict,config)
    output = pd.DataFrame()
    index = 0
    for key in dataDict:
        if len(dataDict[key]) > 0:
            output.loc[index, "Field Name"] = key
            output.loc[index, "Mapped Field Name"] = arraytoString(dataDict[key])
            for j in range(config["PROGRAM"]["EXAMPLES"]):
                output.loc[index, "user"+str(j)] = df.loc[j, dataDict[key][0]]
        index = index + 1
    return output


# In[306]:


builddf().to_csv("MappedFields.csv")


# In[ ]:





# In[ ]:




