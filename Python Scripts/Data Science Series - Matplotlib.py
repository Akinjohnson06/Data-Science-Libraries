#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


#Data
dev_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]


# # Line Plot

# In[3]:


# line plot
plt.plot(dev_x, dev_y);


# In[4]:


# giving a title to the whole graph
plt.plot(dev_x, dev_y)
plt.title('Median Salary (USD) by Age');


# In[5]:


# labeling X and Y axis
plt.plot(dev_x, dev_y)
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)');


# In[6]:


# adding 2 or more lines in one graph
# the Data
dev_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
dev_z = [45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640]

# the code
plt.plot(dev_x, dev_y) 
plt.plot(dev_x, dev_z)
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)');


# In[7]:


# adding legend to the graph 1
plt.plot(dev_x, dev_y) 
plt.plot(dev_x, dev_z)
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.legend(['All Devs', 'Python']);


# In[8]:


# adding legend to the graph 2
plt.plot(dev_x, dev_y, label='All Devs') 
plt.plot(dev_x, dev_z, label='Python')
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.legend();


# In[9]:


# adding different colours and markers to the line 1 (format string)
# fmt= '[marker][line][color]'
plt.plot(dev_x, dev_y, 'x--k', label='All Devs') 
plt.plot(dev_x, dev_z, 'o-b', label='Python')
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.legend();


# In[10]:


# adding different colours and markers to the line 2 (arguments)

plt.plot(dev_x, dev_y, color='k', linestyle='--', marker='o', label='All Devs') 
plt.plot(dev_x, dev_z, color='b', marker='x', label='Python')
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.legend();


# In[11]:


# increase the width of the line
# the default number is 1
plt.plot(dev_x, dev_y, color='k', linestyle='--', marker='o', linewidth=3, label='All Devs') 
plt.plot(dev_x, dev_z, color='b', marker='x', linewidth=9, label='Python')
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.legend();


# In[12]:


# putting in a gridline

plt.plot(dev_x, dev_y, color='k', linestyle='--', marker='o', linewidth=1, label='All Devs') 
plt.plot(dev_x, dev_z, color='b', marker='x', linewidth=1, label='Python')
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.legend()
plt.grid(True);


# In[13]:


# Matplotlib style
# Lets see the available stlye in Matplotlib

plt.style.available


# In[14]:


# Lets use a style

plt.style.use('seaborn-v0_8-colorblind')
plt.plot(dev_x, dev_y, color='k', linestyle='--', marker='o', linewidth=1, label='All Devs') 
plt.plot(dev_x, dev_z, color='b', marker='x', linewidth=1, label='Python')
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.legend()
plt.grid(True);


# In[15]:


# Lets remove some editing so we can see our styles better

plt.style.use('seaborn-v0_8-colorblind') #different style.. 
# Note!!! I haven't really understood the concept of the style yet
plt.plot(dev_x, dev_y, label='All Devs') 
plt.plot(dev_x, dev_z, label='Python')
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.legend();

#plt.grid(True);


# # Bar Chat

# In[16]:


# Bar chat

#plt.style.use('fast'); #different style
plt.bar(dev_x, dev_y, label='All Devs') 
#plt.bar(dev_x, dev_z, label='Python')
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.legend();


# In[24]:


# mixing bar and plot together

plt.bar(dev_x, dev_y, color='g', label='All Devs')
plt.plot(dev_x, dev_z, color='b', label='Python')
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.legend()
plt.grid(True);


# In[18]:


# joining 2 or more bars together (side by side)- without a numpy library
# quite complex
dev_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
dev_z = [45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640]

# Calculate the x-coordinates for the bars
x = range(len(dev_x))
width = 0.35

# Plotting the bars
plt.bar(dev_x, dev_y, width, label='All Devs')
plt.bar([i + width for i in dev_x],dev_z, width, label='Python')


plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.legend()
plt.grid(True);


# In[19]:


# joining 2 or more bars together (side by side)- with a numpy library
# quite complex also
import numpy as np
dev_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
dev_z = [45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640]

# Calculate the x-coordinates for the bars
x = np.arange(len(dev_x))
width = 0.35

# Plotting the bars
plt.bar(dev_x, dev_y, width, label='All Devs')
plt.bar([i + width for i in dev_x],dev_z, width, label='Python')


plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.legend()
plt.grid(True);


# In[20]:


# Stacking bars on top each other

categories = ['Category 1', 'Category 2', 'Category 3']
bar1_values = [10, 15, 12]
bar2_values = [8, 10, 14]

# Plotting the stacked bars
plt.bar(categories, bar1_values, label='Bar 1')
plt.bar(categories, bar2_values, bottom=bar1_values, label='Bar 2')

# Adding labels and a legend
plt.xlabel('Categories')
plt.ylabel('Values')
plt.legend()

# Display the plot
plt.show()


# In[21]:


# adding ticks ()
# joining 2 or more bars together (side by side)- without a numpy library
# quite complex
dev_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
dev_z = [45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640]

# Calculate the x-coordinates for the bars
x = range(len(dev_x))
width = 0.35

# Plotting the bars
plt.bar(dev_x, dev_y, width, label='All Devs')
plt.bar([i + width for i in dev_x],dev_z, width, label='Python')


plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.xticks(ticks=dev_x, labels=dev_x)
plt.legend()
plt.grid(True);


# # Pie chat

# In[25]:


# basic example
plt.style.use('fivethirtyeight')
plt.title('My Pie Plot')
slices = [70 ,30]
plt.pie(slices);


# In[26]:


# add labels

plt.style.use('fivethirtyeight')
plt.title('My Pie Plot')
slices = [70 ,30]
labels = ['70%','30%']
plt.pie(slices, labels=labels);


# In[27]:


# adding seperators to the chat

plt.style.use('fivethirtyeight')
plt.title('My Pie Plot')
slices = [70 ,30]
labels = ['70%','30%']
plt.pie(slices, labels=labels, wedgeprops={'edgecolor':'black'}); #notice the black edge in the chat


# In[33]:


# change colors to the slices

plt.style.use('fivethirtyeight')
plt.title('My Pie Plot')
slices = [120, 80, 30, 20]
labels = ['50%','40%','30%','10%']
colors = ['blue', 'red', 'yellow', 'green']
plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor':'black'}); #notice the black edge in the chat


# In[34]:


# change colors to the slices
# you can actually allow for deafault colours by not specifying

plt.style.use('fivethirtyeight')
plt.title('My Pie Plot')
slices = [120, 80, 30, 20]
labels = ['50%','40%','30%','10%']
#colors = ['blue', 'red', 'yellow', 'green']
plt.pie(slices, labels=labels, wedgeprops={'edgecolor':'black'}); #notice the black edge in the chat


# In[38]:


# Using a more realistic data

plt.style.use('fivethirtyeight')
plt.title('Percentage Of Tech bros in Nigeria')
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript','SQL','HTML','Python','Java']
colors = ['blue', 'red', 'yellow', 'green', 'pink']
plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor':'black'}); #notice the black edge in the chat


# In[40]:


# pick out a particular section to stand out

plt.style.use('fivethirtyeight')
plt.title('Percentage Of Tech bros in Nigeria')
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript','SQL','HTML','Python','Java']
colors = ['blue', 'red', 'yellow', 'green', 'pink']
exp = [0,0,0,0,0.1]#the 0.1 is the length at which it comes out, and the position also matters to get the specific location
plt.pie(slices, labels=labels, colors=colors, explode=exp, wedgeprops={'edgecolor':'black'}); 


# In[41]:


# adding shadow to the chat for a little 3d look

plt.style.use('fivethirtyeight')
plt.title('Percentage Of Tech bros in Nigeria')
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript','SQL','HTML','Python','Java']
colors = ['blue', 'red', 'yellow', 'green', 'pink']
exp = [0,0,0,0,0.1]#the 0.1 is the length at which it comes out, and the position also matters to get the specific location
plt.pie(slices, labels=labels, colors=colors, shadow=True, explode=exp, wedgeprops={'edgecolor':'black'}); 


# In[42]:


# changing the angle of the chat

plt.style.use('fivethirtyeight')
plt.title('Percentage Of Tech bros in Nigeria')
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript','SQL','HTML','Python','Java']
colors = ['blue', 'red', 'yellow', 'green', 'pink']
exp = [0,0,0,0,0.1]#the 0.1 is the length at which it comes out, and the position also matters to get the specific location
plt.pie(slices, labels=labels, colors=colors, shadow=True, startangle=90, explode=exp, wedgeprops={'edgecolor':'black'});
# notice how the chat rotated


# In[43]:


# adding proportional percentage to piechat

plt.style.use('fivethirtyeight')
plt.title('Percentage Of Tech bros in Nigeria')
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript','SQL','HTML','Python','Java']
colors = ['blue', 'red', 'yellow', 'green', 'pink']
exp = [0,0,0,0,0.1]#the 0.1 is the length at which it comes out, and the position also matters to get the specific location
plt.pie(slices, labels=labels, 
        colors=colors, shadow=True, 
        autopct='%1.1f%%',startangle=90,
        explode=exp, wedgeprops={'edgecolor':'black'});
# notice how the chat rotated


# # Stack Plot

# In[2]:


# data

minutes = [1,2,3,4,5,6,7,8,9]

p1 = [1,2,3,3,4,4,4,4,5]
p2 = [1,1,1,1,2,2,2,3,4]
p3 = [1,1,1,2,2,2,3,3,3]


# In[3]:


# Basic stck plot

plt.stackplot(minutes, p1, p2, p3)
plt.title('My Stack Plot');


# In[6]:


# adding labels
labels = ['p1','p2','p3']

plt.stackplot(minutes, p1, p2, p3, labels=labels)
plt.title('My Stack Plot')
plt.legend();


# In[11]:


# move the legend to the top left
labels = ['p1','p2','p3']

plt.style.use('fast')
plt.stackplot(minutes, p1, p2, p3, labels=labels)
plt.title('My Stack Plot')
plt.legend(loc='upper left'); # set in the location here


# In[19]:


# adding colors
#plt.figure(figsize=(6,3)) #size of the whole graph
labels = ['p1','p2','p3']
colors = ['green','red','blue']

plt.style.use('fast')
plt.stackplot(minutes, p1, p2, p3, labels=labels, colors=colors)
plt.title('My Stack Plot')
plt.legend(loc='upper left'); # set in the location here


# In[25]:


# a more realistic data

minutes = [1,2,3,4,5,6,7,8,9]

p1 = [8,6,5,5,4,2,1,1,0]
p2 = [0,1,2,2,2,4,4,4,4]
p3 = [0,1,1,1,2,2,3,3,4]



plt.figure(figsize=(8,3)) #size of the whole graph
labels = ['p1','p2','p3']
colors = ['green','red','blue']

plt.style.use('fast')
plt.stackplot(minutes, p1, p2, p3, labels=labels, colors=colors)
plt.title('My Stack Plot')
plt.legend(loc=(0.07, 0.05)); # set in the location here


# # Filling area on lineplot

# In[28]:


# the Data
ages = [25,26,27,28,29,30,31,32,33,34,35]
avg = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
mean  = [45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640]


# In[45]:


plt.plot(ages, avg, label='average')
plt.fill_between(ages, avg)
plt.title('Something')
plt.xlabel('Ages')
plt.ylabel('Average')
plt.legend();


# In[44]:


plt.plot(ages, mean, label='Mean')
plt.fill_between(ages, mean)
plt.title('Something')
plt.xlabel('Ages')
plt.ylabel('Mean')
plt.legend();


# In[55]:


plt.plot(ages, mean, label='Mean', linewidth=2)
plt.plot(ages, avg, label='Average', linewidth=1)
plt.fill_between(ages, mean, alpha=0.2)
plt.fill_between(ages, avg, alpha=0.2)
plt.title('Something')
plt.xlabel('Ages')
plt.ylabel('Mean')
plt.legend();


# # Histogram

# In[ ]:




