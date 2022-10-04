#!/usr/bin/env python
# coding: utf-8

# Preparations
# For the preparations we will import the necessary libraries which are required for EDA

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv(r"C:\Users\Jayesh.nikam\Downloads\Master.csv")


# In[3]:


data.head()


# In[4]:


data.info()


# From the available informations, we have different features available for exploratory analysis.
# Now we can check how rental rate is distributed.

# In[5]:


print(data['amount'].describe())
plt.figure(figsize=(9, 8))
sns.distplot(data['amount'], color='g', bins=10, hist_kws={'alpha': 1});


# From the above figure we can see that the amount paid by customers mostly lies in between 1 to 10 region.

# In[6]:


print(data['rental_duration'].describe())
plt.figure(figsize=(9, 8))
sns.distplot(data['rental_duration'], color='g', bins=10, hist_kws={'alpha': 1});


# With this information we can see that the rental duration data is uniformly distributed.

# Numerical data distribution
# For this part lets look at the distribution of all of the features by ploting them

# In[7]:


list(set(data.dtypes.tolist()))


# In[8]:


data_num = data.select_dtypes(include = ['float64', 'int64'])
data_num.head()


# 5 rows and 14 columns
# Now lets plot them all:

# In[9]:


data_num.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8);


# Features such as 'customer_id', 'address_id', 'rental_id', 'inventory_id', 'film_id', 'length' and 'payment_id' sharing similar distribution. 

# Correlation
# Now we'll try to find which features are strongly correlated with Amount. We'll store them in a var called golden_features_list. We'll reuse our data_num dataset to do so.

# In[10]:


data_num_corr = data_num.corr()['amount'][:-1] # -1 because the latest row is SalePrice
golden_features_list = data_num_corr[abs(data_num_corr) > 0.5].sort_values(ascending=False)
print("There is {} strongly correlated values with amount:\n{}".format(len(golden_features_list), golden_features_list))


# Now lets take the features we excluded from our correlation table and plot them to see if they show some kind of pattern.

# In[11]:


for i in range(0, len(data_num.columns), 5):
    sns.pairplot(data=data_num,
                x_vars=data_num.columns[i:i+5],
                y_vars=['amount'])


# We can see relationships of most of the parameters with the amount paid by customers and if we look closely at the data we can see that a lot of data points are distributed uniformly.

# In[12]:


data.shape


# In[13]:


data.describe()


# In[14]:


data.columns


# In[15]:


data.nunique()


# In[16]:


data.isnull().sum()


# In return_date section 183 Null value represents till the moment customers haven't returned the dvd.

# Feature to feature relations
# 
# If we try to plot all the numerical features in a seaborn pairplot will take us too much time and will be hard to interpret. We can try to see if some variables are linked between each other and then explain their relation with observation.

# In[18]:


corr = data_num.drop('amount', axis=1).corr()
plt.figure(figsize=(12, 10))

sns.heatmap(corr[(corr >= 0.5) | (corr <= -0.4)], 
            cmap='viridis', vmax=1.0, vmin=-1.0, linewidths=0.1,
            annot=True, annot_kws={"size": 8}, square=True);


# As for release year values closer to zero means there is no linear trend between the two variables. The values of customer_id, address_id and rental_id close to 1 so they are more positively correlated and it shows strong relationship.
