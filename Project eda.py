#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[2]:


df=pd.read_csv("C:/Users/91960/Downloads/used_cars_data.csv")
df.head(5)


# In[3]:


df.tail(6)


# In[4]:


df.dtypes


# In[5]:


df=df.drop(['Location','Seats'],axis=1)
df.head(5)


# In[6]:


df=df.rename(columns={"Kilometers_Driven":"KIlometers","Fuel_Type":"Type","Owner_Type":"Owner"})
df.head(5)


# In[7]:


df.shape


# In[8]:


duplicate_rows_df=df[df.duplicated()]
print("No of duplicate rows",duplicate_rows_df.shape)


# In[9]:


df.count()


# In[10]:


print(df.isnull().sum())


# In[11]:


df=df.dropna()
df.count()


# In[12]:


print(df.isnull().sum())


# In[13]:


sns.boxplot(x=df['Mileage'])


# In[15]:


df.Mileage.value_counts().nlargest(40).plot(kind='bar',figsize=(10,5))
plt.title("Number of cars by making production")
plt.ylabel("No.of cars")
plt.xlabel("Mileage of cars")


# In[17]:


plt.figure(figsize=(10,5))
data=df.corr()
sns.heatmap(data,cmap="Honda Jazz V",annot=True)
data


# In[21]:


fig,axis=plt.subplots(figsize=(10,6))
axis.scatter(df['Engine'],df['Mileage'])
axis.set_xlabel('Engine')
axis.set_ylabel('Mileage')
plt.show()


# In[ ]:




