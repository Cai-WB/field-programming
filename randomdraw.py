# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:26:42 2018

@author: 14194
"""
import os 
import random
import math 

file = open('C:\\Users\\14194\\Desktop\\record.txt')
l = []
result = [1,2,3,4,5,6]
def randomNum():
    for n in range(7):
        a = random.randint(1,100)
        l.append(a)
    f = random.sample(l[:-1],2)
    a,b = f[0],f[1]
    return a,b
def fun_1(a,x,b):
    return a*x+b
def fun_2(x,y):
    return x+y
def fun_3(x,y):
    return x*y
def fun_4(a,x,b):
    return a*x*x+b
def run_draw():
    for n in range(6):
        a,b = randomNum()
        for i in range(4):
            randnum = random.randint(1,4)
            if randnum == 1:
                result[n] = fun_1(a,l[-1],b)
            if randnum == 2:
                result[n] = fun_2(a,b)
            if randnum == 3:
                result[n] = fun_3(a,b)    
            if randnum == 4:
                result[n] = fun_1(a,l[-1],b)
    print(result)
            
                
            
            
            
        
        

    

    
    
        