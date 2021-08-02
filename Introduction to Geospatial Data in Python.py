#!/usr/bin/env python
# coding: utf-8

# ### Introduction to Geospatial Data in Python

# ### Adapted from datacamp by Duong Vu

# In[ ]:


### Plotting the path of hurricane florrence from August 30th to September 18th


# In[6]:


get_ipython().run_line_magic('pip', 'install wheel')
get_ipython().run_line_magic('pip', 'install pipwin')


# In[9]:


import numpy as np


# In[10]:


import pandas as pd


# In[12]:


import rtree


# In[72]:


# load all important packages
import geopandas as gpd
import numpy as np
import pandas as pd
from shapely.geometry import Point

import missingno as msn
import seaborn as sns
import matplotlib as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import sys


# In[6]:


'gdal' in sys.modules


# In[14]:


'geopandas' in sys.modules


# In[13]:


get_ipython().system('pipwin install geopandas')


# In[29]:


import geopandas as gpd


# In[15]:


get_ipython().system('pipwin install fiona')


# In[16]:


get_ipython().system('pipwin install gdal')


# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import scipy


# In[4]:


import rtree


# In[13]:


get_ipython().system('pip install osgeo')


# In[34]:


# getting to know geojson file
country = gpd.read_file(r"C:/Users/husni/Desktop/datacamp/introduction to geospatial data/gz_2010_us_040_00_5m.json")


# In[85]:


country.head()


# In[36]:


type(country)


# In[37]:


type(country.geometry)


# In[38]:


type(country.geometry[0])


# In[86]:


country.plot()


# In[42]:


# Exclude Alaska and Hawaii for now
country[country['NAME'].isin(['Alaska', 'Hawaii']) == False].plot(figsize=(30,20), color='blue')


# In[87]:


florence = pd.read_csv(r'C:\Users\husni\Desktop\datacamp\introduction to geospatial data\florence.csv')


# In[88]:


florence.head()


# In[46]:


florence.info()


# In[47]:


# notice you can always adjust the color if the visualization
msn.bar(florence, color='darkolivegreen')


# In[48]:


# statisctical information
florence.describe()


# In[89]:


# dropping all unused feautures
florence = florence.drop(['AdvisoryNumber', 'Forecaster', 'Received'], axis=1)


# In[90]:


florence.head()


# In[91]:


# add "-" in front of the number to correctly plot the data
florence['Long'] = 0 -florence['Long']


# In[92]:


florence.head()


# In[93]:


# combining lattitude and Longitude to write hurricane coordinates
florence['coordinates'] = florence[['Long', "Lat"]].values.tolist()
florence.head()


# In[56]:


from shapely.geometry import Point


# In[94]:


# change the coordinates to a geopoint
florence['coordinates'] = florence['coordinates'].apply(Point)
florence.head()


# In[59]:


type(florence)


# In[60]:


type(florence['coordinates'])


# In[95]:


# convert the count df to geodf
florence = gpd.GeoDataFrame(florence, geometry='coordinates')
florence.head()


# In[62]:


type(florence)


# In[63]:


type(florence['coordinates'])


# In[96]:


# filtering from before the hurricane was named
florence[florence['Name'] == 'Six']


# In[65]:


# grouping by name to see how many it has in the data set
florence.groupby('Name').Type.count()


# In[69]:


# finding the mean wind speed of hurrican florence
print("Mean wind speed of Hurricane Florence is {} mph and it can go up to {} mph maximum".format(round(florence.Wind.mean(),4),florence.Wind.max()))


# In[97]:


florence.plot(figsize=(20,10))


# In[74]:


import matplotlib.pyplot as plt


# In[98]:


# plotting to see the hurricane overlay the US map
fig, ax = plt.subplots(1, figsize=(30,20))
base = country[country['NAME'].isin(['Alaska', 'Hawaii']) == False].plot(ax=ax, color='blue')

# ploting the hurricane position on top with red color to stand out
florence.plot(ax = base, color = "darkred", marker='*', markersize=10)


# In[100]:


fig, ax = plt.subplots(1, figsize=(20,20))
base = country[country['NAME'].isin(['Alaska', 'Hawaii']) == False].plot(ax=ax, color='blue')
florence.plot(ax = base, column = 'Wind', marker='<', markersize=10, cmap='cool', label='Wind speed(mph)')
_= ax.axis('off')
plt.legend()
ax.set_title("Hurricane Florence in US Map", fontsize=25)
plt.savefig("Hurricane_footage.png", bbox_inches='tight')


# In[ ]:




