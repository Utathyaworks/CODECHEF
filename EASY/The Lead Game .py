#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[10]:


t=int(input())
c1,c2=0,0
gl=-10
f=0
while t:
    p1,p2=map(int,input().split())
    c1+=p1
    c2+=p2
    
    if c1>c2:
        l=c1-c2
        if l>gl:
            gl=l
            f=1
    else:
        l=c2-c1
        if l>gl:
            gl=l
            f=2
    t-=1
print(f,gl)
    

