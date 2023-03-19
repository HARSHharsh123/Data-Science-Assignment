#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Q1Which keyword is used to create a function? Create a function to return a list of odd numbers in the
range of 1 to 25.'''
#Answer -> def keyword is used to create functions ....

def odd():
    l = []
    for i in range(0,26):
        if(i%2!=0):
            l.append(i)
    return l          


# In[5]:


odd()


# In[2]:


'''Q2.Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
to demonstrate their use.'''

#Answer -> we use *agrs and **kwargs when we are unsure of how many arguments are passed during function call 

#demonstartion of *agrs
#args is used for dynamic defination of function 
def demo(*args):
    return args
demo(2,3,2)


# In[3]:


#Q2.
#demonstration of **kwargs
def demo1(**kwargs):
    return kwargs
demo1(a=[1,2,3,4],b=23,c=23.454,d = "Harsh Shukla")


# In[4]:


'''Q3.What is an iterator in python? Name the method used to initialise the iterator object and the method
used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,
16, 18, 20].'''

#Anser ->  iterator is just like pointers that point to the base element of interable object ....
# iter() method is used to initialise the iterator object
# next() method is used for iteration.....
def Method(l,n):
    new_list = []
    item = iter(l)
    while n:
        new_list.append(next(item))
        n-=1
    return new_list
l = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(Method(l,5))



# In[ ]:





# In[5]:


'''Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator
function.'''
#answer -> generator function is a function that produces itrator object for a large sequence of Series.............
#generator function manily behaves like a itrator function 

#yield keyword is used to return the value to the invoker taking a pause to the function 

#example of genrator like if we have to produce the first 10 even numbers:::
def even_number(n):
    i = 1
    while n:
        yield i*2
        i +=1
        n-=1
it = even_number(10)
even_list = []
while True:
    try:
        even_list.append(next(it))
    except StopIteration:
        break;

print(even_list)


# In[5]:


'''Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
first 20 prime numbers.'''

def prime_no(n):
    i = 2
    for i in range(2,n+1):
        c=0
        for j in range(1,n+1):
            if(i%j==0):
                c+=1
        if(c==2):
            yield i
it = prime_no(20)
prime_list = []
while True:
    try:
        prime_list.append(next(it))
    except StopIteration:
        break
print(prime_list)
        


# In[6]:


'''Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.'''
def fibonacci(n):
    a , b = 0,1
    while n:
        yield a
        c = a+b
        a = b
        b = c
        n-=1
it = fibonacci(10)
fibo = []
while True:
    try:
        fibo.append(next(it))
    except StopIteration:
        break
print(fibo)


# In[7]:


'''Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’.
Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']'''
string = "pwskills"
l1 = []
[l1.append(i) for i in string]
print(l1)


# In[8]:


'''Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.'''
lst = list(range(101))
[i for i in lst if i%2==1]


# In[12]:


'''Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.'''
a = int(input("Enter a number  :  "))
d = a
rev = 0
while(a!=0):
    rem = a%10
    rev = (rev*10) + rem
    a = int(a)/10
    a = int(a)
if(d == rev):
    print(d," is a palindrome number")
else:
    print(d," is a not palindrome number")


# In[ ]:




