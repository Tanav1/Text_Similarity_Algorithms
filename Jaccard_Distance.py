#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy import spatial

dataSetI = [1, 0, 0, 1, 0]
dataSetII = [1, 0, 1, 1, 0]
result = 1 - spatial.distance.cosine(dataSetI, dataSetII)


# In[2]:


result


# In[3]:


import numpy as np

def jaccard_binary(x,y):
    """A function for finding the similarity between two binary vectors"""
    intersection = np.logical_and(x, y)
    union = np.logical_or(x, y)
    similarity = intersection.sum() / float(union.sum())
    return similarity

# Define some binary vectors


# Find similarity among the vectors
simxy = jaccard_binary(dataSetI,dataSetII)
print(simxy)


# In[ ]:




