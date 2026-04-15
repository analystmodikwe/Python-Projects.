#!/usr/bin/env python
# coding: utf-8

#                                                             DATA CLEANING

# In[ ]:





# In[6]:


import pandas as pd


# In[8]:


df = pd.read_excel(r"C:\Users\lmodi\OneDrive\Documents\Customer Call List.xlsx")
df


# In[11]:


df = df.drop_duplicates()
df


# In[12]:


df = df.drop(columns = 'Not_Useful_Column')
df


# In[13]:


df['Last_Name'] = df['Last_Name'].str.strip('123./_')
df


# In[14]:


df["Phone_Number"] = df["Phone_Number"].str.replace(r'\D', '', regex=True)
df


# In[15]:


df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' +  x[6:10])  
df


# In[16]:


df["Phone_Number"] = df["Phone_Number"].str.replace('nan--', '')
df["Phone_Number"] = df["Phone_Number"].str.replace('--', '') 
df


# In[18]:


df[["Street_Address","State" ,"Zip_Code"]] = df["Address"].str.split (',',n=2, expand = True)
df


# In[20]:


df['Paying Customer'] = df['Paying Customer'].str.replace('Yes', 'Y')
df['Paying Customer'] = df['Paying Customer'].str.replace('No', 'N')

df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes', 'Y')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No', 'N')
df


# In[21]:


df = df.replace('N/a', '')
df


# In[22]:


df = df.fillna('')
df


# In[23]:


# client asked for a list of all contacts they can call which is all customers with N on the 'Do_Not_Contact' column

for x in df.index:
   if df.loc[x, 'Do_Not_Contact'] ==  'Y':
       df.drop(x, inplace=True)
df



# In[24]:


for x in df.index:
   if df.loc[x, 'Phone_Number']==  '':
       df.drop(x, inplace=True)
df


# In[25]:


df = df.reset_index(drop=True)
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




