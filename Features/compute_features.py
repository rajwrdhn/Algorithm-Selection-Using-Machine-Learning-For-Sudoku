#!usr/var/python
import os
import numpy as np
import pandas as pd 
from scipy import stats
import scipy
from scipy.spatial import distance

class feature_computations():
    def __init__(self, df, N, **kwargs):
        self.df = df
        self.size = N
        
    def add_numberOfNumbers(self):
        #print(np.percentile(df_np, 80))
        counter = 0

        for i in range(self.N):
            for j in range(self.N):
                if (self.df[i][j] > 0):
                    counter += 1 
            
        return counter
    
    def add_MeanofPuzzle(self):
        a = np.mean(self.df)
        return a 
    
    def add_MedianOfPuzzle(self):        
        m = np.median(self.df)
        return m
    
    def add_ModeOfPuzzle(self):
        m = stats.mode(self.df, axis =None)        
        return m

    def add_AverageOfPuzzle(self):
        a = np.average(self.df)
        return a 

    def add_SumOfNumbers(self):
        s = np.sum(self.df)
        return s

    def add_Percentile80(self):
        p = np.percentile(self.df, 80)
        return p

    def add_Percentile70(self):
        p = np.percentile(self.df, 70)
        return p 

    def add_Percentile55(self):
        p = np.percentile(self.df, 55)
        return p     
    
    def add_Percentile45(self):
        p = np.percentile(self.df, 45)
        return p 
        
    def add_manhattan_distance(self):
        li = self.calculate_points()
        #p = distance.cityblock(self.df, self.df)
        p = distance.pdist(self.df)
        print(type(p) , p)
        return p 
        
    def calculate_points(self):
        li = self.df.tolist()
        return li
