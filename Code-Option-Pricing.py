#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:33:51 2020

@author: minayuan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *
import datetime 
import statistics as s
import seaborn as sns
from scipy.stats import * 

# Part 1 Visualize Stock with GMB
call = np.zeros(10)
for i in range(1,11):
    call[i-1] = np.mean(STOCKGBM(s0 = 88, r = 0.04, sigma = 0.18, t = i,size = 1000))

plt.plot(np.arange(0,11),np.hstack((88,call)))
plt.title('Simulation of Sn, n= 1:10, S0 = 88')
plt.show

step = np.linspace(10/1000,10,1000)
call2 = np.zeros(len(step))
for i in range(1000):
    call2[i] = np.mean(STOCKGBM(s0 = 88, r = 0.04, sigma = 0.18, t = step[i],size = 1000))

plt.plot(np.hstack((0,step)),np.hstack((88,call2)),label='1000 steps')
plt.plot(np.arange(0,11),np.hstack((88,call)),label='10 steps')
plt.legend(loc = 'upper left')
plt.title('Simulation of St, t = [1,10], S0 = 88')

def STOCKGBM (s0 = 88, r=0.04, sigma = 0.2, t = 5/365, size = 1000000):
    return(s0*np.exp(sigma*normal(0,np.sqrt(t),size=size)+ \
                     (r-0.5*sigma**2)*t))
    
call3 = np.zeros(10)
for i in range(1,11):
    call3[i-1] = np.mean(STOCKGBM(s0 = 88, r = 0.04, sigma = 0.35, t = i,size = 1000))


call4 = np.zeros((len(step),6))
for n in range(6):
    for i in range(1000):
        call4[i,n] = np.mean(STOCKGBM(s0 = 88, r = 0.04, sigma = 0.35, t = step[i],size = 1)) # change size to have more simulation


for i in range(6):
    plt.plot(np.hstack((0,step)),np.hstack((88,call4[:,i])),label='1000 steps',alpha=0.9)
plt.plot(np.arange(0,11),np.hstack((88,call3)),label='10 steps')
plt.legend(loc = 'upper left')
plt.title('Simulation of St, t = [1,10], S0 = 88')





# Part 2 Price European Call - BSM
def BSMCALL (s0 = 88, r=0.04, sigma = 0.2, t = 5/365, k = 100):
    d1 = (np.log(s0/k)+(r+0.5*sigma**2)*(t))/(sigma*np.sqrt(t))
    d2 = d1 - sigma*np.sqrt(t)
    price = s0*norm.cdf(d1) - k*np.exp(-r*t)*norm.cdf(d2)
    return(price)
    
BSMCALL()
BSMCALL(t=5)

# Part 2 Monte Carlo 
# t = days
def STOCKGBM (s0 = 88, r=0.04, sigma = 0.2, t = 5/365, size = 1000000):
    return(s0*np.exp(sigma*normal(0,np.sqrt(t),size=size)+ \
                     (r-0.5*sigma**2)*t))

def EURCALL (stock , k = 100, t = 5/365, r = 0.04):
    payoff = stock - k 
    payoff[np.where(payoff < 0)] = 0
    price = np.exp(-r*t)*np.mean(payoff)
    return(price)
    
EURCALL(STOCKGBM())
EURCALL(STOCKGBM(t=5),t=5)


# Part 2 Monte Carlo with variance reduction
# my accuracy before reduction
abs(BSMCALL(t=5)-EURCALL(STOCKGBM(t=5),t=5))

# new variance reduction pricing function: antithetic variates
def STOCKGBM2 (s0 = 88, r=0.04, sigma = 0.2, t = 5/365, size = 1000000):
    W1 = normal(loc=0,scale=np.sqrt(t),size=size)
    W2 = -W1
    C1= s0*np.exp(sigma*W1+ (r-0.5*sigma**2)*t)
    C2= s0*np.exp(sigma*W2+ (r-0.5*sigma**2)*t)
    return([C1,C2])

def EURCALL2 (stock , k = 100, t = 5/365, r = 0.04):
    payoff1 = stock[0] - k 
    payoff2 = stock[1] - k
    payoff1[np.where(payoff1 < 0)] = 0
    payoff2[np.where(payoff2 < 0)] = 0
    
    sample = (payoff1+payoff2)/2
    price = np.exp(-r*t)*np.mean(sample)
    return(price)

# my accuracy after reduction
abs(BSMCALL(t=5) - EURCALL2(STOCKGBM2(t=5),t=5))






# Part 3 American VS European Put with Same Characteristics
# Binomial Pricing Function
def trees(u,d,s0,n,k,p,dt,op,optype,r):
    n = int(n)
    N = int(n+1)
    stock  = np.zeros(shape = (int(N),N))
    option  = np.zeros(shape = (int(N),N))
    stock[0,0] = s0
    
    for i in range(1,N):
#        print("stock step",i)
        totalmove = i
        for j in range(totalmove+1):
#            print("stock col",j)
            stock[i,j] = s0 * u**(totalmove - j) * d**(j)
    
    if optype == "eur":
#        print("option step",n)
        if op=="call":
            payoff = stock[i,:] - k
        elif op=="put":
            payoff = k - stock[i,:]
            
        payoff = [max(x,0) for x in payoff]
        option[n,:] = payoff
        
        for i in range(n-1,-1,-1):
#            print("option step",i)
            for j in range(i+1):
#                print("option col",j)
                option[i,j] = np.exp(-r*dt)*(p*option[i+1,j] + (1-p)*option[i+1,j+1])
    
    elif optype == "am":
        if op=="call":
            payoff = stock[i,:] - k
        elif op=="put":
            payoff = k - stock[i,:]
        
        payoff = [max(x,0) for x in payoff]
        option[n,:] = payoff
        
        for i in range(n-1,-1,-1):
#            print("option step",i)
            for j in range(i+1):
#                print("option col",j)
                cont = np.exp(-r*dt)*(p*option[i+1,j] + (1-p)*option[i+1,j+1])
                
                if op =="call":
                    exerpayoff = stock[i,j] - k
                elif op == "put":
                    exerpayoff = k - stock[i,j]
                
                exer = max(exerpayoff, cont)
                option[i,j] = max(cont,exer)
                
    return([stock,option,option[0,0]])

s = np.arange(80,124,4)

r = 0.05
vol =  0.3
k = 100
T = 1 
n = 500
dt = T/n
u = np.exp(vol*np.sqrt(dt)) 
d = np.exp(-vol*np.sqrt(dt)) 
p = 0.5 + 0.5 * (((r-vol**2/2)*np.sqrt(dt))/vol) 
eurput = np.zeros(len(s))
amput = np.zeros(len(s))
for i in range(len(s)):
    eurput[i] = trees(u = u,d=d,s0 = s[i],n= 500,k = 100, p = p, dt = dt, op = "put",optype = "eur", r = r)[2]
    amput[i] = trees(u = u,d=d,s0 = s[i],n= 500,k = 100, p = p, dt = dt, op = "put",optype = "am", r = r)[2]

plt.bar(s,amput, label = 'American Put',color = "red")
plt.bar(s,eurput,label="European Put",color = "blue")   
plt.xlabel("Current stock prices S0")
plt.ylabel("Option Price")
plt.legend()
