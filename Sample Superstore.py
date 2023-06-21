#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Importing Necessary libraries
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings(action="ignore")


# In[3]:


# Read and understand the dataset and check the first five rows
df_superstore=pd.read_csv("SampleSuperstore.csv")
df_superstore.head(10)


# In[4]:


df_superstore.tail(10)


# In[5]:


# Checking the rows and columns of the dataset
df_superstore.shape


# In[6]:


df_superstore.describe()


# In[7]:


#Type of Category
df_superstore["Category"].unique()


# In[8]:


#Type of Sub-Category
df_superstore["Sub-Category"].unique()


# In[9]:


df_superstore.info()


# In[10]:


# Calculating the missing values in the dataset
(df_superstore.isnull().mean()*100).sort_values(ascending=False)


# In[11]:


# we dont have any missing values, so there is certain columns that is not efficient to the dataset
df_superstore.drop(['Postal Code'], axis=1, inplace=True)


# In[12]:


df_superstore.head()


# 
# Number of products in each category

# In[13]:


df_superstore["Category"].value_counts()


# In[14]:


#Total number of products in Categories
df_superstore["Category"].value_counts().sum()


# In[15]:


df_superstore["Sub-Category"].value_counts()


# Unique data in each column

# In[15]:


for col in df_superstore:
    print(df_superstore[col].unique())


# No. of duplicate values in data

# In[16]:


df_superstore.duplicated().sum()


# In[17]:


df_superstore.drop_duplicates()


# Data Visualization

# In[20]:


df_superstore.hist(bins=10, figsize=(18,10))


# Bar Plot Between Sub-category vs Category

# In[22]:


plt.figure(figsize=(16,8))
plt.bar("Sub-Category","Category", data=df_superstore)
plt.show()


# 1. In Furniture Categorythe frequency of individual item is very less.
# 2.In Office supplies the frequency of individual item is medium.
# 3. In Technology the frequency of individual item is high.

# Pie Chart for Sub-Category

# In[24]:


plt.figure(figsize=(12,10))
df_superstore["Sub-Category"].value_counts().plot.pie(autopct="%1.1f%%")
plt.show()


# The samplestore data has wide variety of supplies in Binders and Paper's

# State Vs Count

# In[32]:


#State
plt.figure(figsize=(25,12))
Data=sns.countplot(x="State", data=df_superstore)
Data.set_xticklabels(Data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('State', fontsize=50) 
plt.ylabel('Count', fontsize=50)
plt.show()


# State wise Sales

# In[52]:


plt.figure(figsize=(30,18))
state = df_superstore.groupby(['State'])['Sales'].mean().reset_index()
Data=sns.barplot(x = 'State', y='Sales', data=df_superstore)
Data.set_xticklabels(Data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('State', fontsize=50) 
plt.ylabel('Mean Sales', fontsize=50)
plt.show()


# Profit Vs State

# In[37]:


plt.figure(figsize=(30,18))
state1 = df_superstore.groupby(['State'])['Profit'].mean().reset_index()
data=sns.barplot(x = 'State', y='Profit', data=state1)
data.set_xticklabels(data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('State', fontsize=50) 
plt.ylabel('Mean Profit', fontsize=50)
plt.show()


# Count plot for Category

# In[38]:


plt.figure(figsize=(20,10))
data=sns.countplot(x="Category", data=df_superstore)
data.set_xticklabels(data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Category', fontsize=30) 
plt.ylabel('Count', fontsize=30)
plt.show()  


# Category wise Sales

# In[41]:


plt.figure(figsize=(20,10))
category = df_superstore.groupby(['Category'])['Sales'].mean().reset_index()
data=sns.barplot(x = 'Category', y='Sales', data=category)
data.set_xticklabels(data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Category', fontsize=30) 
plt.ylabel('Mean Sales', fontsize=30)
plt.show()


# Category Vs Profit

# In[43]:


plt.figure(figsize=(20,10))
category2 = df_superstore.groupby(['Category'])['Profit'].mean().reset_index()
data=sns.barplot(x = 'Category', y='Profit', data=category2)
data.set_xticklabels(data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Category', fontsize=30) 
plt.ylabel('Mean Profit', fontsize=30)
plt.show()


# Discount Vs Category

# In[53]:


plt.figure(figsize=(20,10))
category1 = df_superstore.groupby(['Category'])['Discount'].mean().reset_index()
data=sns.barplot(x = 'Category', y='Discount', data=category1)
data.set_xticklabels(data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Category', fontsize=30) 
plt.ylabel('Mean Discount', fontsize=30)
plt.show()


# Count plot for Sub-Category

# In[54]:


plt.figure(figsize=(20,10))
data=sns.countplot(x="Sub-Category", data=df_superstore)
data.set_xticklabels(data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Sub-Category', fontsize=30) 
plt.ylabel('Count', fontsize=30)
plt.show()  


# Sales for Sub-Category

# In[55]:


plt.figure(figsize=(20,10))
subcate = df_superstore.groupby(['Sub-Category'])['Sales'].mean().reset_index()
data=sns.barplot(x = 'Sub-Category', y='Sales', data=subcate)
data.set_xticklabels(data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Sub-Category', fontsize=30) 
plt.ylabel('Mean Sales', fontsize=30)
plt.show()


# Discount for Sub-Category

# In[57]:


plt.figure(figsize=(20,10))
subcate = df_superstore.groupby(['Sub-Category'])['Discount'].mean().reset_index()
data=sns.barplot(x = 'Sub-Category', y='Discount', data=subcate)
data.set_xticklabels(data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Sub-Category', fontsize=30) 
plt.ylabel('Mean Discount', fontsize=30)
plt.show()


# Profit Vs Sub-Category

# In[58]:


plt.figure(figsize=(20,10))
subcate = df_superstore.groupby(['Sub-Category'])['Profit'].mean().reset_index()
data=sns.barplot(x = 'Sub-Category', y='Profit', data=subcate)
data.set_xticklabels(data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Sub-Category', fontsize=30) 
plt.ylabel('Mean Profit', fontsize=30)
plt.show()


# Count plot for Region

# In[59]:


plt.figure(figsize=(20,10))
data=sns.countplot(x="Region", data=df_superstore)
data.set_xticklabels(data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Region', fontsize=30) 
plt.ylabel('Count', fontsize=30)
plt.show()


# Sales Vs Region 

# In[60]:


plt.figure(figsize=(20,10))
region = df_superstore.groupby(['Region'])['Sales'].mean().reset_index()
data=sns.barplot(x = 'Region', y='Sales', data=region)
data.set_xticklabels(data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Region', fontsize=30) 
plt.ylabel('Mean Sales', fontsize=30)
plt.show()


# Discount Vs Region

# In[61]:


plt.figure(figsize=(20,10))
region = df_superstore.groupby(['Region'])['Discount'].mean().reset_index()
data=sns.barplot(x = 'Region', y='Discount', data=region)
data.set_xticklabels(data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Region', fontsize=30) 
plt.ylabel('Mean Discount', fontsize=30)
plt.show()


# Profit Vs Region

# In[63]:


plt.figure(figsize=(20,10))
region = df_superstore.groupby(['Region'])['Profit'].mean().reset_index()
data=sns.barplot(x = 'Region', y='Profit', data=region)
data.set_xticklabels(data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Region', fontsize=30) 
plt.ylabel('Mean Profit', fontsize=30)
plt.show()


# Count plot for ship mode

# In[45]:


plt.figure(figsize=(20,10))
data=sns.countplot(x="Ship Mode", data=df_superstore)
data.set_xticklabels(data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Ship Mode', fontsize=30) 
plt.ylabel('Count', fontsize=30)
plt.show()


# Shipmode Vs Discount

# In[50]:


plt.figure(figsize=(20,10))
shipmode = df_superstore.groupby(['Ship Mode'])['Discount'].mean().reset_index()
data=sns.barplot(x = 'Ship Mode', y='Discount', data=shipmode)
data.set_xticklabels(data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Ship Mode', fontsize=30) 
plt.ylabel('Mean Discount', fontsize=30)
plt.show()


# Shipmode Vs Profit

# In[47]:


plt.figure(figsize=(20,10))
shipmode = df_superstore.groupby(['Ship Mode'])['Profit'].mean().reset_index()
data=sns.barplot(x = 'Ship Mode', y='Profit', data=shipmode)
data.set_xticklabels(data.get_xticklabels(),rotation=90)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Ship Mode', fontsize=30) 
plt.ylabel('Mean Profit', fontsize=30)
plt.show()


# Insights

# 1.Standard class Ship Mode has highest orders.
# 
# 2.Some Data in Ship mode has lowest number of orders it would be better if we try to increase them by some discount in sevices
# 
# 3.From West Region there are more number of orders and profits are also high in West Region, need to concentrate on south as there are less orders
# 
# 4.Copiers sub-category has highest sales ans has maximum profit from sub-categories,we need to make a plan so that we can do to increase the sales and profits of other sub-categories also.
# 
# 5.Technology Category has highes sales and maximum profit ,need to concentate on Office Supplies category to increase sales.
# 
# 6.California State has highest sales but it doesn't have highest profits so we need to make sure that we make considerable profits from this state.
# 
# 7.Vermont State has less number of orders but make best average Profit we need to make sure we have more number of orders.
# 
# 8.Arizona,Texas,Tennessee,,North Carolina,illinois,Florida,Colorado make sure you do not have loss in these states.
