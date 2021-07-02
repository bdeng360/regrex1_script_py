#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


import scipy as sci


# In[4]:


from scipy import stats


# In[5]:


regrex = pd.read_csv("regrex1.csv")


# In[6]:


x = regrex.x


# In[7]:


y = regrex.y


# In[8]:


plt.plot(x, y, 'o')


# In[9]:


reg = stats.linregress(x, y)


# In[10]:


plt.plot(x, y, 'o', label='scatter')
plt.plot(x, reg.intercept + reg.slope*x, 'b', label='lin fit')
plt.legend()