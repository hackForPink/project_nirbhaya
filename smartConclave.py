#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
countries = pd.read_excel('HFA_375_EN.xlsx', sheet_name='Countries')
Data_pivoted = pd.read_excel('HFA_375_EN.xlsx', sheet_name='Data (pivoted)')
Data_pivoted = Data_pivoted.replace(np.nan,0)


# In[3]:


# smart Conclave function
def top_zone(df, countries):
    meanValue = df.mean()
    vulnerable = {}
    for ind in df.index:
        if(df[2016][ind] > meanValue[2016]):
            vulnerable[df['COUNTRY_REGION'][ind]]= df[2016][ind] 
    return vulnerable
vulnerable_regions = top_zone(Data_pivoted, countries)


# In[8]:


Output = {}
for ind in countries.index:
    for key,value in vulnerable_regions.items():
        if countries['Code'][ind] == key:
            Output[countries['Full name'][ind]] = value
print('According to given data following are most vulnerable zone: ')
for i in Output:
    print(i)


# In[9]:


pd.Series(Output).plot.bar()


# In[10]:


pd.Series(Output).plot()


# In[ ]:




