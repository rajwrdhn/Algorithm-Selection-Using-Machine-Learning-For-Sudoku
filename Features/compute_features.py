#!usr/var/python
import os
import numpy as np
import pandas as pd 
from scipy import stats


class feature_computations():
    def __init__(self, df, N, **kwargs):
        self.df = df
        self.size = N
        
    def add_numberOfNumbers(self, df_np, N):
        #print(np.percentile(df_np, 80))
        counter = 0

        for i in range(N):
            for j in range(N):
                if (df_np[i][j] > 0):
                    counter += 1 
            
        return counter
    
    def add_MeanofPuzzle(self, df_np, N):
        a = np.mean(df_np)
        return a 
    
    def add_MedianOfPuzzle(self, df_np, N):        
        m = np.median(df_np)
        return m
    
    def add_ModeOfPuzzle(self, df_np, N):
        m = stats.mode(df_np, axis =None)        
        return m

    def add_AverageOfPuzzle(self, df_np, N):
        a = np.average(df_np)
        return a 

    def add_SumOfNumbers(self, df_np, N):
        s = np.sum(df_np)
        return s

    def add_Percentile80(self, df_np, N):
        p = np.percentile(df_np, 80)
        return p

    def add_Percentile70(self, df_np, N):
        p = np.percentile(df_np, 70)
        return p 

    def add_Percentile55(self, df_np, N):
        p = np.percentile(df_np, 55)
        return p     
    
    def add_Percentile45(self, df_np, N):
        p = np.percentile(df_np, 45)
        return p 
        
        
