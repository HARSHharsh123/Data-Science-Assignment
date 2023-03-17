#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1. Explain with an example each when to use a for loop and a while loop.
#example of for loop 
lst = [1,2,3,4,5]
for i in lst:
    print(i)


# In[2]:


#example of while loop (printing list in reverse order
lst = [1,2,3,4,5]
s = len(lst)-1
while(s!=-1):
    print(lst[s])
    s = s -1


# In[3]:


'''Q2.Write a python program to print the sum and product of the first 10 natural numbers using for
and while loop.'''
#using for loop
su = 0
pro = 1
for i in range(1,11):
    su+=i
    pro*=i
print(su,pro)


# In[4]:


#using while loop
su = 0
pro = 1
i=1
while(i!=11):
    su+=i
    pro*=i
    i+=1
print(su,pro)


# In[5]:


'''Q3. Create a python program to compute the electricity bill for a household.
The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per
unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.
You are required to take the units of electricity consumed in a month from the user as input.
Your program must pass this test case: when the unit of electricity consumed by the user in a month is
310, the total electricity bill should be 2250.'''

units = int(input("Enter the electricity units consumed in a month"))
if(units <=100):
    total = (units * 4.5)
elif(units <= 200):
    total = (100*4.5) + (units - 100)*6
elif(units <= 300):
    total = (100*4.5)+(100*6)+(units - 200)*10
else:
    total = (100*4.5) + (100 * 6) + (100 * 10) + (units - 300)*20
print(total)


# In[6]:


'''Q4.Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print
that list.'''
#using for loop 
new_list = []
import math
l = list(range(1,100))
for i in l:
    cube = math.pow(i,3)
    if(cube%4==0 or cube%5==0):
        new_list.append(i)
print(new_list)


# In[7]:


#using for while loop 
new_list = []
import math
i=1
while(i<100):
    cube = math.pow(i,3)
    if(cube%4==0 or cube%5==0):
        new_list.append(i)
    i= i + 1
print(new_list)


# In[8]:


'''Q5. Write a program to filter count vowels in the below-given string.
string = "I want to become a data scientist"'''

count=0
string = "I want to become a data scientist"
for i in string:
    if(i=='a'or i=='e'or i=='i'or i=='o'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U'):
        count+=1
print(count)


# In[9]:


print("Assignment First Completed BY HARSH SHUKLA")

