#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd


# In[3]:


# all dataframes from 2018-19


# In[5]:


dfNov = pd.read_csv("JC-201811-nov-citibike-tripdata.csv")
dfNov.head()


# In[6]:


dfDec = pd.read_csv("JC-201812-dec-citibike-tripdata.csv")
dfDec.head()


# In[7]:


dfJan = pd.read_csv("JC-201901-jan-citibike-tripdata.csv")
dfFeb = pd.read_csv("JC-201902-feb-citibike-tripdata.csv")
dfMar = pd.read_csv("JC-201903-march-citibike-tripdata.csv")
dfApr = pd.read_csv("JC-201904-april-citibike-tripdata.csv")
dfMay = pd.read_csv("JC-201905-may-citibike-tripdata.csv")


# In[13]:


dfJan.head()


# In[14]:


dfFeb.head()


# In[15]:


dfMar.head()


# In[16]:


dfApr.head()


# In[17]:


dfMay.head()


# In[18]:


citiBike_data_7_months_2018_19 = pd.concat([dfNov, dfDec, dfJan, dfFeb, dfMar, dfApr, dfMay])


# In[19]:


citiBike_data_7_months_2018_19.head()


# In[20]:


citiBike_data_7_months_2018_19


# In[ ]:





# In[21]:


citiBike_data_7_months_2018_19.to_csv("citiBike_data_7_months_2018_19.csv", sep = ",")


# In[ ]:




