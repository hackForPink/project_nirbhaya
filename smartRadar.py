#!/usr/bin/env python
# coding: utf-8

# In[62]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')
report=pd.read_excel('HFA_375_EN.xlsx')
report.head()


# In[63]:


countries = pd.read_excel('HFA_375_EN.xlsx', sheet_name='Countries')


# In[64]:


countries.head()


# In[65]:


country_groups = pd.read_excel('HFA_375_EN.xlsx', sheet_name='Country groups')
country_groups.head()


# In[66]:


country_groups_mapping = pd.read_excel('HFA_375_EN.xlsx', sheet_name='Country groups mapping')
country_groups_mapping.head()


# In[67]:


notes = pd.read_excel('HFA_375_EN.xlsx', sheet_name='Measure notes')
notes.head()


# In[68]:


Data_table = pd.read_excel('HFA_375_EN.xlsx', sheet_name='Data (table)')
Data_table.head()


# In[69]:


Data_pivoted = pd.read_excel('HFA_375_EN.xlsx', sheet_name='Data (pivoted)')
Data_pivoted = Data_pivoted.replace(np.nan,0)
Data_pivoted.head()


# In[70]:


Data_table.groupby('COUNTRY_REGION').plot.bar()


# In[71]:


Data_pivoted.at[0,2016]


# In[76]:


# smart Radar function
def top_zone(df, countries):
    meanValue = df.mean()
    vulnerable = {}
    for ind in df.index:
        if(df[2016][ind] > meanValue[2016]):
            vulnerable[df['COUNTRY_REGION'][ind]]= df[2016][ind] 
    return vulnerable
vulnerable_regions = top_zone(Data_pivoted, countries)
sorted_regions = {k: v for k, v in sorted(vulnerable_regions.items(), key=lambda item: item[1], reverse=True)}
sorted_regions


# In[81]:


Output = []
for ind in countries.index:
    for key in sorted_regions:
        if countries['Code'][ind] == key:
            Output.append(countries['Full name'][ind])
print('According to given data following are most vulnerable zone: ')
for i in Output:
    print(i)


# In[ ]:




