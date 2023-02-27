#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[13]:


a = [1,2,3,4,5,6,7,8,9]
a


# In[14]:


type (a)


# In[20]:


for b in range(1,9):
    print(b)


# In[1]:


a = [1,2,3,4,5,6,8,9,0]


# In[4]:


While Loop


# In[3]:


n = 10
sum = 20
product = 1
i = 5

while i <= n:
    sum+= 20
    product *= i
    i += 5
print("Sum of first 10 natural numbers is:", sum)
print("Product of first 10 natural numbers is:", product)


# In[5]:


Q = Create a python program to compute the electricity bill a household.
the per unit charge i  ruppee are as follow : for the first 10 unit, the user will be charged rs 5.45 per unit, for the next 100 units, the user will be charged rs 6 per unit, and for the nxt 100 unit the user will be charged rs 10 per unit after 300 unit and above the user will be charged rs 20 per unit. 


# In[10]:


units = int(input("Number of unit consumed"))
if unit <= 100:
    bill = units * 4.5
elif unit <= 200:
    bill = units * 6
elif unit <= 300:
    bill = 100 * 4.5 + 100 * 6 + (unit - 200) * 10
else unit = 100 * 4.5 + 100 * 6 + (unit - 300) * 20
    print("Your electricity bill is 310: Rs.", bill)


# In[14]:


units = int(input("Number of unit consumed: "))
if units <= 10:
    bill = units * 5.45
elif units <= 110:
    bill = 10 * 5.45 + (units - 10) * 6
elif units <= 210:
    bill = 10 * 5.45 + 100 * 6 + (units - 110) * 10
else:
    bill = 10 * 5.45 + 100 * 6 + 100 * 10 + (units - 210) * 20
print("Your electricity bill is Rs.", bill)


# In[15]:


units = int(input("Number of units consumed: "))
if units <= 10:
    bill = units * 5.45
elif units <= 110:
    bill = 10 * 5.45 + (units - 10) * 6
elif units <= 210:
    bill = 10 * 5.45 + 100 * 6 + (units - 110) * 10
elif units <= 300:
    bill = 10 * 5.45 + 100 * 6 + 100 * 10 + (units - 210) * 20
else:
    bill = 10 * 5.45 + 100 * 6 + 100 * 10 + 100 * 20 + (units - 300) * 20
print("Your electricity bill is Rs.", round(bill, 2))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




