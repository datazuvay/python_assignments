#!/usr/bin/env python
# coding: utf-8

# In[5]:


n = int(input("Please enter a number: "))
count = 0

for i in range(1, n+1):
    if not (n % i) :
        count += 1
        
if (n == 0) or (n == 1) or (count >= 3):
    print(n, "is not a prime number")
else:
    print(n, "is a prime number")


# In[ ]:




