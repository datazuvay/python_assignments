#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list = []
for number in range(1, 101):
    if number % 3 == 0 and number % 5 != 0:
        number = "Fizz"
        my_list.append(number)
    
    elif number % 5 == 0 and number % 3 !=0:
        number = "Buzz"
        my_list.append(number)
    elif number % 3 == 0 and number % 5 == 0:
        number = "FizzBuzz"
        my_list.append(number)
    else:
        my_list.append(number)
    print(number)


# In[ ]:




