#!/usr/bin/env python
# coding: utf-8

# In[2]:


sentence = input("Please give a sentence: ")
x = {} #start with an empty dict
for i in sentence:
    if i not in x:
        x[i] = 0
    x[i] += 1 
print(x)


# In[ ]:




