#!/usr/bin/env python
# coding: utf-8

# In[1]:


# since seaborn is built of matplotlip, we actually need to also import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# In[2]:


x = [10, 20, 30, 40]
y = [0, 15, 10, 25]


# In[3]:


plt.figure(figsize=(5,3.5))
plt.plot(x,y);


# In[4]:


sns.set()


# In[5]:


plt.figure(figsize=(5,3.5))
plt.plot(x,y);


# In[6]:


# setting styles

sns.set_style('white')


# In[7]:


plt.figure(figsize=(5,3.5))
plt.plot(x,y);


# In[8]:


sns.set_style('whitegrid')
plt.figure(figsize=(5,3.5))
plt.plot(x,y);


# In[9]:


sns.set_style('dark')
plt.figure(figsize=(5,3.5))
plt.plot(x,y);


# In[10]:


sns.set_style('white')
plt.figure(figsize=(5,3.5))
plt.plot(x,y);


# In[11]:


file = r"C:\Users\DELL\Desktop\seaborn-data-master\seaborn-data-master\mpg.csv"


# In[12]:


car = pd.read_csv(file)


# In[13]:


car.head()


# In[14]:


sns.relplot(x='model_year', y='mpg',  col='origin', hue='cylinders',data=car);


# # KDE plot - Kernel Density Estimation
# 
# ### non- parametric
# ### biverate

# In[15]:


# non-parametric

plt.figure(figsize=(4,3));
sns.kdeplot(car['horsepower'], label='horsepower')
plt.legend()


# In[16]:


# shading the area
plt.figure(figsize=(4,3))
sns.kdeplot(car['horsepower'], label='horsepower', fill=True) # it was formally called shade but now its called fill
plt.legend();


# In[17]:


# using bandwidth to show more pick

plt.figure(figsize=(4,3))
sns.kdeplot(car['horsepower'], label='horsepower', bw_method=10, fill=True)
plt.legend();


# In[18]:


# cummulative
plt.figure(figsize=(4,3))
sns.kdeplot(car['horsepower'], label='horsepower', bw_method='scott', cumulative=True, fill=True)
plt.legend(loc='upper left');


# In[19]:


# biverate

sns.set_style('darkgrid')
plt.figure(figsize=(4,3))
sns.kdeplot(x =car.horsepower, y= car.mpg);


# In[20]:


# seeing more granularity

sns.set_style('darkgrid')
plt.figure(figsize=(4,3))
sns.kdeplot(x =car.horsepower, y= car.mpg, n_levels=20);


# In[21]:


# having a shaded version


sns.set_style('darkgrid')
plt.figure(figsize=(4,3))
sns.kdeplot(x =car.horsepower, y= car.mpg, n_levels=20, fill=True, thresh=False);


# In[22]:


# having a shaded version


sns.set_style('darkgrid')
plt.figure(figsize=(4,3))
sns.kdeplot(x =car.horsepower, y= car.mpg, n_levels=20, fill=True);


# In[23]:


# adding color bar

sns.set_style('darkgrid')
plt.figure(figsize=(4,3))
sns.kdeplot(x =car.horsepower, y= car.mpg, n_levels=20, fill=False, cbar=True);


# # Histplot

# In[24]:


# lets load another Data
pen = pd.read_csv(r"C:\Users\DELL\Desktop\seaborn-data-master\seaborn-data-master\penguins.csv")
pen.head()


# In[25]:


pen.shape


# In[26]:


# sum of missing values
pen.isna().sum().sum()


# In[27]:


# droppig missing values
pen.dropna(inplace=True)


# In[28]:


pen.shape


# In[29]:


# ploting histagram

sns.set_style('white')
plt.figure(figsize=(4,3))
sns.histplot(pen.bill_length_mm);


# In[30]:


# ploting histagram 2

sns.set_style('white')
plt.figure(figsize=(4,3))
sns.histplot(x = 'bill_length_mm', data=pen);


# In[31]:


# plotting horizontal histogram

sns.set_style('white')
plt.figure(figsize=(4,3))
sns.histplot(y = 'bill_length_mm', data=pen); # just replace the X with Y


# In[32]:


# adding kde

sns.set_style('white')
plt.figure(figsize=(4,3))
sns.histplot(x = 'bill_length_mm', data=pen, kde=True);


# In[33]:


#bins

sns.set_style('white')
plt.figure(figsize=(4,3))
sns.histplot(x = 'bill_length_mm', data=pen, bins=20);


# In[34]:


# binwidth and binrange

sns.set_style('white')
plt.figure(figsize=(4,3))
sns.histplot(x = 'bill_length_mm', data=pen, binwidth=5, binrange=(30,60));


# ## STATISTICS WITH HIST
# 
# - count (default)
# - density
# - probability

# In[35]:


# count

sns.set_style('white')
plt.figure(figsize=(4,3))
sns.histplot(x = 'bill_length_mm', data=pen, stat= 'count');


# In[36]:


# density

sns.set_style('white')
plt.figure(figsize=(4,3))
sns.histplot(x = 'bill_length_mm', data=pen, stat= 'density'); # take a look at the y axis


# In[37]:


# probability

sns.set_style('white')
plt.figure(figsize=(4,3))
sns.histplot(x = 'bill_length_mm', data=pen, stat= 'probability');


# In[38]:


# probability cummulative

sns.set_style('white')
plt.figure(figsize=(4,3))
sns.histplot(x = 'bill_length_mm', data=pen, stat= 'probability', fill= False, element='step');


# In[39]:


sns.set_style('white')
plt.figure(figsize=(4,3))
sns.histplot(x = 'bill_length_mm', data=pen, stat= 'probability', fill= False, element='step', cumulative=True);


# In[40]:


# adding hue

sns.set_style('white')
plt.figure(figsize=(8,4))
sns.histplot(x = 'bill_length_mm', data=pen, hue='species');


# In[41]:


sns.set_style('white')
plt.figure(figsize=(8,4))
sns.histplot(x = 'bill_length_mm', data=pen, hue='species', element='step');


# In[42]:


sns.set_style('white')
plt.figure(figsize=(8,4))
sns.histplot(x = 'bill_length_mm', data=pen, hue='species', element='poly');


# In[43]:


sns.set_style('white')
plt.figure(figsize=(8,4))
sns.histplot(x = 'bill_length_mm', data=pen, hue='species', multiple='stack');


# In[44]:


sns.set_style('white')
plt.figure(figsize=(8,4))
sns.histplot(x = 'bill_length_mm', data=pen, hue='species', multiple='fill');


# In[45]:


# biverate
sns.set_style('white')
plt.figure(figsize=(8,4))
sns.histplot(x = 'bill_length_mm', y = 'bill_depth_mm', data=pen, hue='species', cbar=True);


# In[46]:


# Styling

sns.set_style('white')
plt.figure(figsize=(8,4))
sns.histplot(x = 'species', data=pen, hue='sex', multiple='dodge');


# In[47]:


sns.set_style('white')
plt.figure(figsize=(8,4))
sns.histplot(x = 'species', data=pen, hue='sex', multiple='dodge', shrink=0.8);


# In[48]:


sns.set_style('white')
plt.figure(figsize=(8,4))
sns.histplot(x = 'species', data=pen, hue='sex', multiple='dodge', shrink=0.8, palette='bone');


# In[49]:


sns.set_style('white')
plt.figure(figsize=(8,4))
sns.histplot(x = 'species', data=pen, hue='sex', multiple='dodge', shrink=0.8, fill=False);


# # ECDF plot - Empirical Cumulative Distribution Function

# In[50]:


# data

tips = pd.read_csv(r"C:\Users\DELL\Desktop\seaborn-data-master\seaborn-data-master\tips.csv")
tips.head()


# In[51]:


# Basic plot
sns.set_style('darkgrid')
sns.ecdfplot(x='tip', data=tips);


# In[52]:


tips['tip'].min(), tips['tip'].max()


# In[53]:


tips['tip'].value_counts().head()


# In[54]:


sns.set_style('darkgrid')
sns.ecdfplot(x='tip', data=tips);
plt.axvline(4, c='black');


# In[55]:


# horizontal

sns.set_style('darkgrid')
sns.ecdfplot(y='tip', data=tips);


# In[56]:


# adding hue

sns.set_style('darkgrid')
sns.ecdfplot(x='tip', data=tips, hue='day');


# In[57]:


# stat - count

plt.figure(figsize=(8,4))
sns.set_style('darkgrid')
sns.ecdfplot(x='tip', data=tips, stat='count',  hue='day');


# In[58]:


# weights

plt.figure(figsize=(8,4))
sns.set_style('darkgrid')
sns.ecdfplot(x='tip', data=tips, stat='count', weights='tip');


# In[59]:


# styling

plt.figure(figsize=(8,4))
sns.set_style('darkgrid')
sns.ecdfplot(x='tip', data=tips, hue='day',palette='summer');


# # Box Plot

# In[60]:


car.head()


# In[61]:


cars = car[car.cylinders.isin([4,6,8])]
cars


# In[62]:


# basics

plt.figure(figsize=(4,4))
sns.set_style('whitegrid')
sns.boxplot(x='mpg', data=cars);


# In[63]:


cars.mpg.describe()


# In[64]:


# basics

plt.figure(figsize=(4,4))
sns.set_style('whitegrid')
sns.boxplot(x='origin', y='mpg', data=cars);


# In[65]:


# adding hue

plt.figure(figsize=(4,4))
sns.set_style('whitegrid')
sns.boxplot(x='origin', y='mpg', hue='cylinders', data=cars);


# In[66]:


# Styling

plt.figure(figsize=(4,4))
sns.set_style('whitegrid')
sns.boxplot(y='origin', x='mpg', data=cars); # swtching the axis


# In[67]:


# order the plot

plt.figure(figsize=(4,4))
sns.set_style('whitegrid')
sns.boxplot(x='origin', y='mpg', order=['japan','europe','usa'],data=cars);


# In[68]:


# Changing plot color

plt.figure(figsize=(4,4))
sns.set_style('whitegrid')
sns.boxplot(x='origin', y='mpg', color='k', data=cars);


# In[69]:


cars['new_model'] = cars['model_year'] > 76


# In[70]:


# Changing plot color with hue

plt.figure(figsize=(4,4))
sns.set_style('whitegrid')
sns.boxplot(x='origin', y='mpg',palette='dark:r', hue='new_model', data=cars);


# In[71]:


# width

plt.figure(figsize=(4,4))
sns.set_style('whitegrid')
sns.boxplot(x='origin', y='mpg', palette='dark:b', hue='new_model', width=0.5, data=cars);


# In[72]:


# linewidth

plt.figure(figsize=(4,4))
sns.set_style('whitegrid')
sns.boxplot(x='origin', y='mpg', palette='dark:r', hue='new_model', linewidth=2.5, width=0.5, data=cars);


# In[73]:


# whis - whisker

# linewidth

plt.figure(figsize=(4,4))
sns.set_style('whitegrid')
sns.boxplot(x='origin', y='mpg', palette='dark:r', hue='new_model', linewidth=2.5, width=0.5, whis=1, data=cars);


# In[74]:


# fliersize

# linewidth

plt.figure(figsize=(4,4))
sns.set_style('whitegrid')
sns.boxplot(x='origin', y='mpg', palette='dark:r', hue='new_model', linewidth=2.5, width=0.5, fliersize=1, data=cars);


# In[75]:


# showcaps

plt.figure(figsize=(4,4))
sns.set_style('whitegrid')
sns.boxplot(x='origin', y='mpg', palette='dark:r', hue='new_model', linewidth=2.5, width=0.5,fliersize=1,
            showcaps=False, data=cars);


# # Violin Plot

# In[76]:


# Basic

plt.figure(figsize=(6,2))
sns.set_style('whitegrid')
sns.violinplot(x = 'displacement', data = cars);


# In[77]:


plt.figure(figsize=(6,4))
sns.set_style('whitegrid')
sns.violinplot(x='cylinders', y='displacement', data=cars);


# In[78]:


# adding hue

plt.figure(figsize=(6,4))
sns.set_style('whitegrid')
sns.violinplot(x='cylinders', y='displacement', hue='origin', data=cars);


# In[79]:


# split

plt.figure(figsize=(6,4))
sns.set_style('whitegrid')
sns.violinplot(x='cylinders', y='displacement', hue='origin', split=True,
               data=cars[cars['origin'].isin(['japan','europe'])])

plt.legend(loc=2);


# In[80]:


# inner

plt.figure(figsize=(6,4))
sns.set_style('whitegrid')
sns.violinplot(x='cylinders', y='displacement', hue='origin', split=True,
               data=cars[cars['origin'].isin(['japan','europe'])], inner='quartile')

plt.legend(loc=2);


# In[81]:


# scaling

plt.figure(figsize=(6,4))
sns.set_style('whitegrid')
sns.violinplot(x='cylinders', y='displacement', hue='origin', split=True,
               data=cars[cars['origin'].isin(['japan','europe'])], density_norm='count')

plt.legend(loc=2);


# # Swamplot

# In[82]:


# Basic

plt.figure(figsize=(6,4))
sns.set_style('whitegrid')
sns.swarmplot(x='horsepower', data=cars);


# In[97]:


# Basic

plt.figure(figsize=(6,4))
sns.set_style('whitegrid')
sns.swarmplot(x='horsepower', data=cars, linewidth=1);


# In[100]:


# Basic

plt.figure(figsize=(6,4))
sns.set_style('whitegrid')
sns.swarmplot(x='horsepower', data=cars, linewidth=1, edgecolor='yellow');


# In[105]:


# Basic

plt.figure(figsize=(6,4))
sns.set_style('whitegrid')
sns.swarmplot(x='horsepower', data=cars, linewidth=1, edgecolor='yellow', marker = 'x');


# In[83]:


# Basic

plt.figure(figsize=(6,4))
sns.set_style('whitegrid')
sns.swarmplot(x='origin', y='horsepower', data=cars);


# In[84]:


# adding hue

plt.figure(figsize=(8,4))
sns.set_style('whitegrid')
sns.swarmplot(x='origin', y='horsepower', hue='cylinders', data=cars);


# In[85]:


# adding dodge

plt.figure(figsize=(8,4))
sns.set_style('whitegrid')
sns.swarmplot(x='origin', y='horsepower', hue='cylinders',dodge=True, data=cars);


# In[86]:


# swarm plot overlay with box plot
usa = cars[cars['origin']=='usa']


# In[87]:


plt.figure(figsize=(8,4))
sns.boxplot(x = usa['cylinders'], y = usa['horsepower'])
sns.swarmplot(x = usa['cylinders'], y = usa['horsepower']);


# In[88]:


# styling
plt.figure(figsize=(8,4))
sns.boxplot(x = usa['cylinders'], y = usa['horsepower'])
sns.swarmplot(x = usa['cylinders'], y = usa['horsepower'], color='black', alpha=0.5);


# In[89]:


# styling
plt.figure(figsize=(8,4))
sns.boxplot(x = usa['cylinders'], y = usa['horsepower'], whis=np.inf)
sns.swarmplot(x = usa['cylinders'], y = usa['horsepower'], color='black', alpha=0.5);


# In[94]:


# swarm plot overlay with violin plot

plt.figure(figsize=(8,4))
sns.violinplot(x = usa['cylinders'], y = usa['horsepower'])
sns.swarmplot(x = usa['cylinders'], y = usa['horsepower'], color='red', alpha=0.3);


# # Strip plot

# In[ ]:


# basics

