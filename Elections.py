#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np


# In[7]:


data = open('city1.txt','r')


# In[8]:


import pandas as pd


# In[9]:


df = pd.read_excel (r'/Users/faaizahdesai/Desktop/City1.xlsx', sheet_name = 'City1')


# In[10]:


print(df)


# In[11]:


CityID = pd.DataFrame(df, columns = ['CityID'])


# In[12]:


print(CityID)


# In[13]:


df['CityID']


# In[14]:


df.shape


# In[15]:


df.head(10)


# In[16]:


df.tail(100)


# In[17]:


df.info()


# In[18]:


df.Term_Start.value_counts()


# In[19]:


trn = df.Turnout.sort_values()
trn


# In[20]:


type(CityID)


# In[21]:


df.CityID == 233


# In[22]:


city = df.CityID.value_counts(ascending=True,dropna = False)
city


# In[23]:


df.sort_values(by=['Turnout','Polls_Close'])


# In[25]:


df[df.CityID == 236]


# In[27]:


df[(df.CityID == 236)&(df.CandID == 195663)]


# In[28]:


df.CityID.value_counts(ascending=True,dropna = False).head(3)


# In[29]:


import matplotlib.pyplot as plt


# In[30]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[31]:


df


# In[32]:


NYC = df[df.CityID == 241]


# In[33]:


NYC


# In[34]:


NYC.CandID.value_counts().plot(kind = 'bar')


# In[35]:


df.Term_Start.value_counts()


# In[36]:


df.sort_values( by = 'Term_Start')


# In[37]:


import seaborn as sns


# In[42]:


list(df.groupby('CityID'))


# In[44]:


for group_key, group_value in df.groupby('CityID'):
    print(group_key)
    print(group_value)


# In[57]:


df.groupby('Polls_Close').size()


# In[77]:


keyrace = df.groupby('Term_Start').agg(['max'])


# In[59]:


df[df.Polls_Close == '2016-06-07']


# In[78]:


keyrace


# In[74]:


df.groupby(['Term_Start','Polls_Close']).size()


# In[86]:


df.groupby(['Term_Start','Polls_Close','Turnout']).agg({'Share':['max']})


# In[88]:


df.loc[df.Term_Start == '1918-02-01'].groupby(['Term_Start','Polls_Close','Turnout']).agg({'Share':['max']})


# In[89]:


df.head()


# In[90]:


df.set_index('Term_Start')


# In[91]:


df.head()


# In[93]:


df.set_index('Share',inplace = True)


# In[95]:


df.head()


# In[98]:


df.sort_index(inplace = True, ascending = False)
df.head


# In[100]:


df.reset_index(inplace = True)


# In[101]:


df.head()


# In[108]:


df.stack()


# In[ ]:




