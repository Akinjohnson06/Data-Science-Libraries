#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# An array is defined as a collection of items that are stored at a contiguous memory locations. It is a container which holds a fixed number of items, and these items should be of the same type.
# 
# A combination of arrays saves a lot of time. The array can be reduce the overall size of the code

# # How to create an array

# In[5]:


arr = np.array([1,2,3,4])
arr


# In[4]:


type(arr)


# In[6]:


# adding another datatype1
arr_1 = np.array([1,2,3,4,5.6]) # i added a float in this array
arr_1 # judging from the result, it converted everything to floats


# In[45]:


# adding another datatype2
arr_1_1 = np.array([1,2,3,4,'One']) # i added a string in this array
arr_1_1# judging from the result, it converted everything to strings


# In[9]:


# adding two list to form a matrics
arr_2 = np.array([[1,2,3,4],[5,6,7,8]])
arr_2


# In[10]:


# adding two list to form a matrics
arr_2_1 = np.array([[1,2,3,4],[5,6,7,8],[1,3,5,7]])
arr_2_1


# # slicing and attributes

# In[12]:


arr = np.array([1,2,3,4])
arr[0:2]


# In[13]:


arr = np.array([1,2,3,4])
arr[:2]


# In[14]:


arr = np.array([1,2,3,4])
arr[2:]


# In[15]:


arr = np.array([1,2,3,4])
arr[::]


# In[16]:


arr = np.array([1,2,3,4])
arr[::2]


# In[19]:


arr = np.array([1,2,3,4])
arr[::-1]


# In[22]:


arr_2 = np.array([[1,2,3,4],[5,6,7,8]])
arr_2[1]


# In[23]:


arr_2 = np.array([[1,2,3,4],[5,6,7,8]])
arr_2[0:2,0:2]


# In[29]:


arr_2 = np.array([[1,2,3,4],[5,6,7,8]])
arr_2[1, 0:3]


# In[32]:


arr_2_1 = np.array([[1,2,3,4],[5,6,7,8],[1,3,5,7]])
arr_2_1[2, 0:2]


# In[35]:


#ATTRIBUTES
# shape give the number of rows and column in an array
np.shape(arr_2_1)
# result means 3 rows and 4 columns


# In[36]:


np.shape(arr_2)


# In[37]:


# size gives the total elements
np.size(arr_2_1)


# In[38]:


np.size(arr_2)


# In[39]:


# dimensions
np.ndim(arr_2_1)


# In[40]:


np.ndim(arr_2)


# In[47]:


# datatype of an array
arr.dtype


# # Python List VS Numpy arrays

# ### NUMPY
# - a list cannot directly handle mathematical operation, while arrays can
# - An array consumes less space
# - Using arrays are faster than list
# - a list can stor different data types while arrays cannot
# 
# ### LIST
# - a list is easier to modify since a list stores each elements individually, it is easier to add and delete an element than an array does
# - in one can have nested data with different size, while you cannot do that in array

# # Creating an array using Numpy Functions

# In[53]:


#ARRANGE FUNCTION
#format=[START][STOP][STEP][DTYPE]
arr = np.arange(1,11,1,dtype=float)
arr


# In[54]:


arr = np.arange(1,11,1,dtype=int)
arr


# In[55]:


arr = np.arange(1,11)
arr


# In[57]:


arr = np.arange(1,11,2)
arr


# In[60]:


#ZERO FUNCTION
#format=[nRows][ncolumns][dtype]
arr = np.zeros((2,2))
arr


# In[64]:


arr = np.zeros((4,2), dtype=float)
arr


# In[65]:


#ONES FUNCTION
#format=[nRows][ncolumns][dtype]
arr = np.ones((2,2))
arr


# In[67]:


arr = np.ones((4,10), dtype=float)
arr


# In[72]:


#FULL FUNCTION
#format=[shape][full_value][dtype]
arr = np.full(10, 8)
arr


# In[73]:


arr = np.full((2,2), 8)
arr


# In[74]:


arr = np.full((10,2), 8, dtype=int)
arr


# In[80]:


#RESHAPE FUNCTION
#format= [nRows][ncolumns][dtype]
arr = np.arange(1,10,1,dtype=int).reshape(3,3)
arr


# In[83]:


arr = np.arange(10).reshape(2,5)
arr


# In[84]:


arr = np.arange(10).reshape(5,2)
arr


# In[89]:


#REPEAT FUNCTION
#format= [value][ntimes][dtype]
arr = np.repeat(50,10)
arr


# In[91]:


arr = np.repeat(50,10)
arr


# In[92]:


arr = np.repeat([[3,2]], 5, axis=1)
arr


# In[93]:


arr = np.repeat([[3,2]], 5, axis=0)
arr


# In[95]:


#CONCATENATE FUNCTION
#format= [value][ntimes][dtype]
arr = np.array([1,2,3,4,5])
arr1= np.array([6,7,8,9,10])

c = np.concatenate([arr,arr1])
c


# In[97]:


arr = np.array([[1,2,3,4,5],[2,4,6,8,10]])
arr1= np.array([[6,7,8,9,10],[1,3,5,7,9]])

c = np.concatenate([arr,arr1])
c


# In[99]:


arr = np.array([[1,2,3,4,5],[2,4,6,8,10]])
arr1= np.array([[6,7,8,9,10],[1,3,5,7,9]])

c = np.concatenate([arr,arr1],axis=1)
c


# In[103]:


# V-STACK AND H-STACK
arr = np.array([[1,2,3,4,5],[2,4,6,8,10]])
arr1= np.array([[6,7,8,9,10],[1,3,5,7,9]])

v = np.vstack([arr,arr1])
v


# In[104]:


h = np.hstack([arr,arr1])
h


# In[112]:


#POWER FUNCTION
#format=[VARIABLE][POWER]
arr = np.array([1,2,3,4])
power = np.power(arr, [2])

print(arr)
print(power)


# In[113]:


arr = np.array([1,2,3,4])
power = np.power(arr, [2,2,4,3]) #specify different powers for each number

print(arr)
print(power)


# In[115]:


#DIFF FUNCTION - also means difference

arr = np.array([1,2,3,4]) #2-1, 3-2, 4-3
arr1 = np.array([2,4,6,8]) # 4-2, 6-4, 8-6

diff = np.diff(arr)
diff1 = np.diff(arr1)

print(arr)
print(diff)
print(diff1)


# In[116]:


arr = np.array([2,4,6,8]) #4-2, 6-4, 8-6
arr1 = np.array([1,5,2,9]) # 5-1, 2-5, 9-2

diff = np.diff(arr)
diff1 = np.diff(arr1)

print(arr)
print(diff)
print(diff1)


# In[119]:


arr = np.array([2,4,6,8]) #4-2, 6-4, 8-6
arr1 = np.array([1,5,2,9]) # 5-1, 2-5, 9-2

diff = np.diff((arr,arr1), axis=0) # arr1 - arr
diff1 = np.diff((arr1,arr), axis=0)# arr- arr1

print(diff)
print(diff1)


# In[121]:


#CROSS FUNCTION

arr = np.array([2,4]) 
arr1 = np.array([1,5])

# basically the calculation is ((2*5)-(4*1)) 

c = np.cross(arr,arr1)
c


# In[126]:


#SORT FUNCTION

arr = np.array([6,2,10,8]) 
arr1 = np.array([7,5,2,9])

s = np.sort((arr,arr1))
s


# In[127]:


arr = np.array([6,2,10,8]) 
arr1 = np.array([7,5,2,9])

print(arr)
print(arr1)
s = np.sort((arr,arr1))
s


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




