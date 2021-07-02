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


print(regrex)


# In[7]:


x = regrex.x


# In[8]:


y = regrex.y


# In[9]:


plt.plot(x, y, 'o')


# In[10]:


reg = stats.linregress(x, y)


# In[11]:


plt.plot(x, reg.intercept + reg.slope*x, 'b', label='lin fit')


# In[12]:


plt.plot(x, y, 'o', label='scatter')
plt.plot(x, reg.intercept + reg.slope*x, 'b', label='lin fit')
plt.legend()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




