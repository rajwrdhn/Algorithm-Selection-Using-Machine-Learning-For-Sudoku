#!usr/var/python3
import os
import math
import numpy as np
import pandas as pd 
from scipy import stats
import scipy
from scipy.spatial import distance

class feature_computations():
    def __init__(self, df, N, name_l):
        self.df = df
        self.size = N
        self.list_deepLearning: list = []
        self.name_ = name_l

    def sizeofpuzzle(self):
        return self.size
    
    def orderofpuzzle(self):
        a = math.sqrt(self.size)
        return a
        
    def add_percentOfNumbers(self):
        #print(np.percentile(df_np, 80))
        counter = 0

        for i in range(self.size):
            for j in range(self.size):
                if (self.df[i][j] > 0):
                    counter += 1 
        if (counter >0 ):
            per = counter * 100/ (self.size* self.size)
        else:
            per = 0
        #print(per)  
        return per
    
    def add_MeanofPuzzle(self):
        a = np.mean(self.df)
        return a 
    
    def add_MedianOfPuzzle(self):        
        m = np.median(self.df)
        return m
    
    def add_ModeOfPuzzle(self):
        a = self.df.ravel()
        m = stats.mode(a, axis =None)        
        return m

    def add_AverageOfPuzzle(self):
        a = np.average(self.df)
        return a 

    def add_SumOfNumbers(self):
        s = np.sum(self.df)
        return s

    def add_Percentile(self):
        p = np.percentile(self.df, 80)
        return p
    
    def add_NumberOfEmptyRows(self):
        #print(self.df)
        #count = 0 
        #for i in range(self.size):
        a = np.size(np.where(~self.df.any(axis=1))[0])
        #for i in range(np.where(~self.df.any(axis=1))[0]):
            #i +=1
        return a #count / (self.size )
    
    def add_NumberOfEmptyColumns(self):
        a = np.size(np.where(~self.df.any(axis=0))[0])
        return a
    
    def add_NumberOfEmptySubBlocks(self):
        return self.df
    
    def add_manhattan_distance(self):
        #li = self.calculate_points()
        k = np.zeros((self.size,self.size)).astype(int).ravel()
        a = self.df.ravel()
        b = np.where(a > 0.5, 1, 0)
        p = distance.cityblock(b, k)
        #p = distance.pdist(self.df)
        #print(type(p) , p)
        return p 
        
    def calculate_points(self):
        li = self.df.tolist()
        return li
    
    def sizeofsmallestrow(self):
        return 0 
    
    def sizeoflargestrow(self):
        return 0 
    
    def sizeofsmallestcolumn(self):
        return 0
    
    def sizeoflargestcolumn(self):
        return 0
    
    def numberofsquares(self):
        return 0 
    
    def numberofrowswith1identicalnumber(self):
        return 0
    
    def numberofrowswith2identicalnumber(self):
        return 0
    
    def numberofcolumnswith1identicalnumber(self):
        return 0
    
    def numberofcolumnswith2identicalnumber(self):
        return 0
    
    def numberofcolumnsfilledcompletely(self):
        return 0 
    
    def numberofrowsfilledcompletely(self):
        return 0
    
    def numberofnumbersindiagonal(self):
        return 0
    
    # transpose of a sudoku and diagonals 

    def calculate_gcp_features(self):
        import graphcolorfeatures
        gcp_model = graphcolorfeatures.GraphColorAsSudoku(self.df,self.size)
        gcp_model.make_puzzle()
        #print(gcp_model.make_puzzle())
        

    def deeplearning1(self):
        #print(self.df)
        #counter = 0
        self.list_deepLearning.append(self.name_)
        for i in range(self.size):
            for j in range(self.size):
                 
                if (self.df[i][j] > 0):
                    #insert 1 into the column as feature
                    self.list_deepLearning.append(1)
                else: #insert 0 into the coilumn as feature
                    self.list_deepLearning.append(0)
        return self.list_deepLearning
    
    def deeplearning2(self):
        #print(self.df)
        #counter = 0
        self.list_deepLearning.append(self.name_)
        for i in range(self.size):
            for j in range(self.size):
                self.list_deepLearning.append(self.df[i][j])
        return self.list_deepLearning