#!/usr/bin/env python
# coding: utf-8

# In[ ]:


t=int(input())
while t:
    c=input()
    if c=="B" or c=="b":
        print("BattleShip")
    elif c=="C" or c=="c":
        print("Cruiser")
    elif c=="D" or c=="d":
        print("Destroyer")
    elif c=="F" or c=="f":
        print("Frigate")
    t-=1

