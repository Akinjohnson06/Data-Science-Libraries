#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Pandas is built on numpy

import pandas as pd


# In[2]:


df = pd.read_csv(r"C:\Users\DELL\Desktop\Libray Series\Pandas\survey_results_public.csv")


# In[3]:


df


# In[4]:


# shape gives you the total rows and column
df.shape


# In[5]:


# info() gives number of rows, column, and data types
df.info()


# In[6]:


# Notice that our dataframe above was truncated. So we were not able to see all of the columns
# See below for code that allows us see all columns
pd.set_option('display.max_columns', 85) # the 85 here is the number of columns you want to display


# In[7]:


# so we run the dataframe again
df


# In[8]:


schema_df = pd.read_csv(r"C:\Users\DELL\Desktop\Libray Series\Pandas\survey_results_schema.csv")


# In[9]:


schema_df


# In[10]:


# Notice that our dataframe above was concatinated. So we were not able to see all of the rows
# See below for code that allows us see all rows
pd.set_option('display.max_rows', 85) # the 85 here is the number of rows you want to display


# In[11]:


schema_df


# In[12]:


# first n rows
df.head()


# In[13]:


# last n rows
df.tail()


# In[14]:


# List of all columns in our dataframe
df.columns 


# In[15]:


# assessing column
df.Hobbyist


# In[16]:


# another way


# In[17]:


df['Hobbyist']


# In[18]:


# to get the count of unique values
df['Hobbyist'].value_counts()


# In[19]:


# assessing rows based on interger location
# we use iloc[]
df.iloc[0] #the first row. 0 meaning integer zero.. which returns a series


# In[20]:


# assessing more than one row based on interger location
# we use iloc[]
df.iloc[[0,1]] #the two rows. 0 meaning integer zero and 1 meaning integer one.. which returns a datframe


# In[21]:


# assessing more than one row, with a specfic column based on interger location
# we use iloc[]
df.iloc[[0,1], 5] #the two rows. 0 meaning index zero, 1 meaning index one and 5 meaning index five for columns
#which returns a series


# In[22]:


# assesing a row based on location
# we use loc[]
df.loc[0]  #the first row. 0 meaning index zero.. which returns a series


# In[23]:


# assessing more than one row based on location
# we use loc[]
df.loc[[0,1]] #the two rows. 0 meaning index zero and 1 meaning index one.. which returns a datframe


# In[24]:


# for iloc[], you have to specify the integer location for the column, but for loc[], you can just type the column name
# assessing more than one row, with a specfic column based on location
# we use loc[]
df.loc[[0,1], 'Employment'] #the two rows. 0 meaning index zero, 1 meaning index one and 5 meaning index five for columns
#which returns a series


# In[25]:


# for iloc[], you have to specify the integer location for the column, but for loc[], you can just type the column name
# assessing more than one row, and more than one columns based on location
# we use loc[]
df.loc[[0,1], ['Employment','MainBranch']] #the two rows. 0 meaning index zero, 1 meaning index one and 5 meaning index five for columns
#which returns a dataframe


# In[26]:


# Data filtering
df['Hobbyist'] == 'Yes'


# In[27]:


# we can assign it to a variable
hob = df['Hobbyist'] == 'Yes'
hob


# In[28]:


# to get a dataframe instead
df[df['Hobbyist'] == 'Yes']


# In[29]:


# you can also add a variable to it
hob_1 = df[df['Hobbyist'] == 'Yes']
hob_1


# In[30]:


high_salary = df[df['ConvertedComp'] > 70000]
high_salary


# In[31]:


high_salary_1 = df['ConvertedComp'] > 70000


# In[32]:


df.loc[high_salary_1]


# In[33]:


df.columns


# In[34]:


df.loc[high_salary_1, ['Country','LanguageWorkedWith','ConvertedComp']]


# In[35]:


# more filtering
countries = ['United States', 'Finland', 'United Kingdom', 'Canada']
high_salary_1 = df[df['Country'].isin(countries)]
high_salary_1


# In[36]:


# OR
countries = ['United States', 'Finland', 'United Kingdom', 'Canada']
high_salary_1 = df['Country'].isin(countries)
df.loc[high_salary_1, 'Country']


# In[37]:


# this colume has different inputs in a cell, seperated with a comma. so we want results that contains a particular result
# e.g 'Python'
df[df['LanguageWorkedWith'].str.contains('Python', na=False)]


# In[38]:


# OR
python = df['LanguageWorkedWith'].str.contains('Python', na=False)
df.loc[python, 'LanguageWorkedWith']

# so basically, youll see that python is common in this list


# In[39]:


# updating rows and columns
# updating columns
# making our column names to be all Capital letters
df.columns = [x.upper() for x in df.columns] #this is a list comprehension
df


# In[40]:


# to normal
df.columns = [x.capitalize() for x in df.columns] #this is a list comprehension
df


# In[41]:


# replacing the spaces in our column names to underscore, or vice-vesar, or with anything
df.columns = df.columns.str.replace(' ', '_')
df


# In[42]:


df.columns


# In[43]:


# to change some columns and not all
df.rename(columns={'RESPONDENT':'SERIAL_NO', 'MAINBRANCH': 'MAIN_BRANCH'}, inplace=True) #inplace make things permanent
df


# In[58]:


# Changin specific columns in a row
# Use this for a much smaller data
# df.loc[2] = [column1, column2, column3, ...]
#but we have a much larger data so we use the below
df.loc[2, 'MAIN_BRANCH'] = 'I am a student'
df


# In[59]:


# SORTING DATA
# Sorting with one column
#df.sort_values(by='HOBBYIST') #automatically it is in ascending order. so to make it in decending order
df.sort_values(by='Hobbyist', ascending=False)


# In[61]:


# sorting with multiple columns
df.sort_values(by=['Hobbyist','Student'], ascending=False)


# In[62]:


# making one column ascending and the other column descending
df.sort_values(by=['Hobbyist','Student'], ascending=[False,True])#use inplace to make it permanent


# In[47]:


# sorting by index
df.sort_index()


# In[63]:


# you can call out a column and sort it
df['Student'].sort_values()


# In[64]:


df['Convertedcomp'].nlargest(10) # to see it in series


# In[65]:


df.nlargest(10, 'Convertedcomp') #to see it in a dataframe


# In[66]:


df['Convertedcomp'].nsmallest(10) # to see it in series


# In[67]:


df.nsmallest(10, 'Convertedcomp') #to see it in a dataframe


# In[53]:


# GROUPING AND AGGREGATION
# the describe method can give us a brief overview of what we want to see
df.describe()


# In[68]:


# median value for a column
df['Convertedcomp'].median()


# In[69]:


# median value for multiple column
df[['Convertedcomp','Age']].median()


# In[70]:


df['Convertedcomp'].count() # this method returns the number of non-null values in a series or Datafram


# In[73]:


df['Convertedcomp'].value_counts() # used to count the frequency of unique values in a panda series


# In[74]:


df


# In[76]:


df['Socialmedia'].value_counts()


# In[77]:


df['Socialmedia'].value_counts(normalize=True)


# In[78]:


# Grouping - Groupby

# we grouping by country. So lets bring the column out first
df['Country'].value_counts()


# In[79]:


country_grp = df.groupby(['Country'])


# In[80]:


country_grp.get_group('Chad')


# In[82]:


filt = df['Country'] == 'India'
df.loc[filt]["Socialmedia"].value_counts()


# In[83]:


country_grp['Socialmedia'].value_counts()


# In[85]:


country_grp['Socialmedia'].value_counts().head(50)


# In[87]:


country_grp['Socialmedia'].value_counts().loc['India']


# In[102]:


k = df.groupby('Country')['Socialmedia']
k.value_counts().loc['United States']


# In[103]:


df.groupby('Country')['Convertedcomp'].median()


# In[104]:


df.groupby('Country')['Convertedcomp'].median().loc['Germany']


# In[105]:


df.groupby('Country')['Convertedcomp'].agg(['median', 'mean'])


# In[106]:


df.groupby('Country')['Convertedcomp'].agg(['median', 'mean']).loc['Canada']


# In[108]:


filt = df['Country'] == 'India'
df.loc[filt]["Languageworkedwith"].str.contains('Python').sum()


# In[ ]:





# In[ ]:





# # Cleaning Data- Casting Datatypes and Handling Missing Values

# In[109]:


import numpy as np


# In[110]:


# creating a dataframe
people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'], 
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}


# In[112]:


df = pd.DataFrame(people)
df


# In[113]:


# droping missing values
df.dropna()
# by default, what it actually did was...
#  df.dropna(axis='index', how='any')


# In[115]:


df = pd.DataFrame(people)

df.replace('NA', np.nan, inplace=True)
df.replace('Missing', np.nan, inplace=True)

df


# In[116]:


df.isna()


# In[117]:


# filling missing values randomly
df.fillna(0) # dont forget to use inplace = True
# i dont want to use it right now because i still want to use the dataset


# In[119]:


df.dtypes
# from the result, we see that the age column is a string instead of an integer. So lets convert it to an int


# In[123]:


#### df['age'] = df['age'].astype(int) # converting to an integer datatype
'''Since the age column has missing values, to convert it to an integer will throw an error. 
So we either fill the missing values or we convert to a float instead.
But in this case i'm going to be converting to a float'''

df['age'] = df['age'].astype(float)


# In[124]:


# so lets check if it changed
df.dtypes


# In[132]:


# now lets take the average/mean of the age column

df['age'].mean()

#We cannont take the average/mean of a string datatype.
#Technically, it doesnt make sense.
#So we convert to an int or a float.


# # Date and Time Series

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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




