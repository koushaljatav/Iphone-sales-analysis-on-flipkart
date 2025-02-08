#!/usr/bin/env python
# coding: utf-8

# # iphone sales analysis in india

# In[1]:


import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
sd=pd.read_csv("apple_products.csv")


# In[2]:


sd.head()


# In[3]:


sd.isnull().sum()


# In[4]:


sd.describe()


# In[5]:


sd.describe().transpose()


# In[6]:


high_rated=sd.sort_values(by=["Star Rating"],ascending=False)


# In[7]:


high_rated


# In[8]:


high_rated.head(10)


# In[9]:


high_rated=high_rated.head(10)


# In[10]:


high_rated


# In[11]:


high_rated['Product Name'].value_counts()


# In[12]:


iphone=high_rated['Product Name'].value_counts()


# In[13]:


label=iphone.index
label


# In[14]:


count=high_rated['Number Of Ratings']
count


# In[15]:


figure=px.bar(high_rated,x=label,y=count,title="Number of rating of Highest Rated Iphone")
figure.show()


# In[16]:


iphone=high_rated['Product Name'].value_counts()
label=iphone.index
count=high_rated['Number Of Reviews']
figure=px.bar(high_rated,x=label,y=count,title="Number of Reviewsg of Highest Rated Iphone")
figure.show()


# In[17]:


figure=px.scatter(data_frame=sd,x="Number Of Ratings",y="Sale Price",
size="Discount Percentage",trendline="ols",
title="Relationship between Sale price and number of rating iphones")
figure.show()


# In[18]:


figure=px.scatter(data_frame=sd,x="Number Of Ratings",y="Discount Percentage",
size="Sale Price",trendline="ols",
title="Relationship between Sale price and number of rating iphones")
figure.show()


# In[ ]:




