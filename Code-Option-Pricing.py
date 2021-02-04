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

def BSMCALL (s0 = 88, r=0.04, sigma = 0.2, t = 5/365, k = 100):
    d1 = (np.log(s0/k)+(r+0.5*sigma**2)*(t))/(sigma*np.sqrt(t))
    d2 = d1 - sigma*np.sqrt(t)
    price = s0*norm.cdf(d1) - k*np.exp(-r*t)*norm.cdf(d2)
    return(price)
    
BSMCALL()
BSMCALL(t=5)

# my accuracy before reduction
abs(BSMCALL(t=5)-EURCALL(STOCKGBM(t=5),t=5))

# variance reduction: antithetic variates
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
