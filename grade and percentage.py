#!/usr/bin/env python
# coding: utf-8

# In[1]:


i=10
j=15
k=8
if i<j:
   if j<k:
    i=j
   else:
        j=k
else:
   if j>k:
      j=i
   else:
      i=k
print("i=",i,"j=","k=,",k)                    


# write a python program that requests an integer value  from  the  user.if the value is between 1 and 100 inclusive ,print  "ok" ,otherwise print "out of range"

# In[29]:


a=int(input())  
if  1<=a<=100:
   print("ok",a)
else:
   print("not in the range")


# In[28]:


val=int(input())
if val < 10:
     if val !=5:
         print(" wow " , end='')
     else:
        val+=1
else:
     if val==17:
         val+=10
     else:
         print("whoa",end='')
print(val)


# write apython  program ,that  request integer value  from user.if  the  value is b/w -1 and -50 print ok,if  the  value is 1 to  50 ,print waoo, if value  is  0 print  try again.

# b=int(input())
# if -50<=b<=-1:
#     print("ok")
# elif 1<=b<=50:
#     print("good")
# elif b==0:
#     print ("try again")
#     

# In[ ]:





# code one
# 

# In[49]:


n=int(input())
if  n<1000:
    print('*')
if  n<100:
    print('*')
if n<10:
    print('*')
if n<=1:
    print('*')
    


# In[ ]:





# code two

# In[48]:


n=int(input())
if  n<1000:
    print('*')
elif  n<100:
    print('*')
elif n<10:
    print('*')
elif n<1:
    print('*')
    


# In[ ]:





# program of marks sheet

# In[8]:


n=input(    "    name of  student:   "   )
p=int(input("   marks obtained in physics:"))
c=int(input("   marks obtained in chemistry:"))
m=int(input("   marks obtained in maths:"))
b=int(input("   marks obtained in biology:"))
i=int(input("   marks obtained in computer:"))
f=(p+c+m+b+i)
print(n)
if 250<=f<=300:
    print("grde E","marks obtained",f)
if 301<=f<=350:
    print("grde D","marks obtained",f)
if 351<=f<=400:
    print("grde C","marks obtained",f)
if 401<=f<=450:
    print("grde B","marks obtained",f)
if 451<=f<=500:
     print("grde A","marks obtained",f)

    
    

    
    


# In[ ]:





# percentage marks sheet

# In[12]:


n=input(    "    name of  student:   "   )
p=int(input("   marks obtained in physics:"))
c=int(input("   marks obtained in chemistry:"))
m=int(input("   marks obtained in maths:"))
b=int(input("   marks obtained in biology:"))
i=int(input("   marks obtained in computer:"))
f=(((p+c+m+b+i)/500)*100)
print(n)
if 41<=f<=50:
    print("grde E","percentage:",f)
if 51<=f<=60:
    print("grde D","percentage:",f)
if 61<=f<=70:
    print("grde C","percentage:",f)
if 71<=f<=80:
    print("grde B","percentage:",f)
if 81<=f<=100:
     print("grde A","percentage:",f)


# In[ ]:




