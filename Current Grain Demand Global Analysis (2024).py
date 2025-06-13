#!/usr/bin/env python
# coding: utf-8

# # This is an explatory data analysis for grain demand globally

# Grains are the world's most staple food. However, grains are produced on a seasonal basis in most regions in the wold. Grains are also consumed all year long with fairly stable demand. The exploratory data analyis conducted in this notebook is therefore important for farmers, consumers, and other stakeholders. 

# In[1]:


#import the libraries needed

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px



# In[2]:


#import the data

grain_df= pd.read_csv(r"C:\Users\Administrator\Downloads\GrainDemandProduction.csv")
grain_df.head()


# In[3]:


#checking the information contained in the dataset

grain_df.info()


# In[4]:


#checking the unique features in each colum

grain_df.nunique()


# In[5]:


#dropping the Dataset column

grain_df= grain_df.drop(["Dataset"], axis=1)


# In[6]:


grain_df.head()


# In[7]:


# setting the index

#grain_df.set_index("Region", inplace=True)

grain_df.head()



# In[8]:


grain_df.groupby('Region').value_counts()

grain_df.groupby('Element')

grain_df.head(10)


# In[ ]:





# In[9]:


#creating a filter for food grain demand for the year 2024

food_grain_df= grain_df["Element"].str.contains("Food") & (grain_df["Year"]==2024)

mask= grain_df[food_grain_df]

mask


# In[10]:


food_grain_mask=mask.groupby("Region").sum().sort_values(by="Millions of metric tons", ascending=False)

food_grain_mask


# In[11]:


#Visualising the above information in a more readable format

food_grain_mask.plot(y="Millions of metric tons", kind="bar")

plt.title("Food Grain Demand Per Region")

plt.xlabel("Region")

plt.ylabel("Millions of Metric tons")


# In[15]:


#other grain demand 
grain_df.head()

other_grain_demand_df= grain_df["Element"].str.contains("Other") & (grain_df["Year"]==2024)

mask_other= grain_df[other_grain_demand_df]

mask_other= mask_other.groupby("Region").sum ().sort_values(by= "Millions of metric tons", ascending=False)

mask_other.head()


# In[17]:


#visualising other types of grain demanded by demand
mask_other.plot(y="Millions of metric tons", kind="bar")

plt.title("Other Grain Demanded Per Region")

plt.xlabel("Region")

plt.ylabel("Millions of Metric tons")


# In[19]:


# implied additional demanded grain 
implied_grain_demand_df= grain_df["Element"].str.contains("Implied") & (grain_df["Year"]==2024)

mask_implied= grain_df[implied_grain_demand_df]

mask_implied= mask_implied.groupby("Region").sum ().sort_values(by= "Millions of metric tons", ascending=False)

mask_implied.head()


# In[20]:


# Grain produced in the various regions 
grain_produced_df= grain_df["Element"].str.contains("production") & (grain_df["Year"]==2024)

mask_produced= grain_df[grain_produced_df]

mask_produced= mask_produced.groupby("Region").sum ().sort_values(by= "Millions of metric tons", ascending=False)

mask_produced.head()


# In[35]:


# combining the various masked dataframes

combined_df= pd.concat([food_grain_mask, mask_other["Millions of metric tons"], mask_implied["Millions of metric tons"],mask_produced["Millions of metric tons"]], axis=1)

combined_df= combined_df.drop(["Year"], axis=1)

#renaming the added columns by order           
combined_df.columns=['Element',
    'Sub-region',
    'Food Grain Demand',
    'Other Grain Demand',
    'Implied Grain Demand',
    'Produced Grain'
                    ]

combined_df


# In[38]:


#Visualising the information in form of a stacked column chart

combined_df.plot(y=["Food Grain Demand", "Other Grain Demand", "Produced Grain", "Implied Grain Demand"], kind="bar", figsize=(10,6))

plt.xlabel("Region")
plt.ylabel("Millions of Metric tons")
plt.title("Current Global Grain Demand by Region")
plt.show()

