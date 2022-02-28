#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 10:52:56 2022

@author: monamez
"""
import numpy as np

#Monte Carlo - Find Stationary Distribution
def MonteCarlo(Adj,n,startState):
    pi = np.array([0,0,0])
    pi[startState] = 1
    prevState = startState
    
    i = 0
    while i < n:
        currState = np.random.choice([0,1,2],p=Adj[prevState])
        pi[currState] += 1
        prevState = currState
        i+= 1
    return pi;

def RepeatedMult(A,n):
    A_n = A
    i = 0
    while i < n:
        A_n = np.matmul(A_n,A)
        i += 1
    print("Repeated Matrix Multiplication yields: ",A_n[0])