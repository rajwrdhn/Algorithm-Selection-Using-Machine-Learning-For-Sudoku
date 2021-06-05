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
        self.order = int(math.sqrt(N))

    def sizeofpuzzle(self):
        return self.size
    
    def orderofpuzzle(self):
        a = math.sqrt(self.size)
        return a
    
    def sumof(self):
        for i in range(self.size):
            i = i +1
        
        return i
        
    def percentofnumbers(self):
        counter = 0

        for i in range(self.size):
            for j in range(self.size):
                if (self.df[i][j] > 0):
                    counter += 1 
        if (counter >0 ):
            per = counter * 100/ (self.size* self.size)
        else:
            per = 0  
        return per
    
    def meanofpuzzle(self):
        a = np.mean(self.df)
        return a 
    
    def medianofpuzzle(self):        
        m = np.median(self.df)
        return m
    
    def modeofpuzzle(self):
        a = self.df.ravel()
        m = stats.mode(a, axis =None)        
        return m

    def averageofpuzzle(self):
        a = np.average(self.df)
        return a 

    def sumofnumbers(self):
        s = np.sum(self.df)
        return s

    def percentilepuzzle(self):
        p = np.percentile(self.df, 80)
        return p
    
    def manhattandistance(self):
        k = np.zeros((self.size,self.size)).astype(int).ravel()
        a = self.df.ravel()
        b = np.where(a > 0.5, 1, 0)
        p = distance.cityblock(b, k)
        return p 
        
    def calculate_points(self):
        li = self.df.tolist()
        return li
    
    #get subgrids helper
    def getsubgrids(self):
        d = self.df
        subgrids = []
        for box_i in range(self.order):
            for box_j in range(self.order):
                subgrid = []
                for i in range(self.order):
                    for j in range(self.order):
                        subgrid.append(d[self.order*box_i + i][self.order*box_j + j])
                subgrids.append(subgrid)
        return subgrids 
    
    def sizeofsmallestsubgrid(self):        
        p = self.getsubgrids()
        mina = self.size
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd < mina):
                mina = xd
        return mina

    def sizeoflargestsubgrid(self):        
        p = self.getsubgrids()
        maxa = 0
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd > maxa):
                maxa = xd
        return maxa
    
    def minmaxsubgrid(self):
        p1 = self.sizeofsmallestsubgrid()
        p2 = self.sizeoflargestsubgrid()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2
    
    def minsdsubgrid(self):
        p1 = self.sizeofsmallestsubgrid()
        p2 = self.size

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2

    def numberofsubgridsfilledcompletely(self):
        p = self.getsubgrids()
        count = 0
        for x in p:
            xd = [i for i in x if i > 0]
            if (len(xd) == self.size):
                count += 1
        return count
    
    def numberofsubgridsempty(self):
        p = self.getsubgrids()
        count = 0
        for x in p:
            xd = [i for i in x if i==0]
            if (len(xd)==self.size):
                count += 1
        return count 

    def sizeofsmallestrow(self):
        p = self.df.tolist()
        mina = self.size
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd < mina):
                mina = xd
        return mina
    
    def sizeoflargestrow(self):
        p = self.df.tolist()
        maxa = 0
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd > maxa):
                maxa = xd
        return maxa 
    
    def minmaxrow(self):
        p1 = self.sizeofsmallestrow()
        p2 = self.sizeoflargestrow()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2 
    
    def minsdrow(self):
        p1 = self.sizeofsmallestrow()
        p2 = self.size

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2   
    
    def sizeofsmallestcolumn(self):
        #do same like row after transpose
        p = self.df.transpose().tolist()
        mina = self.size
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd < mina):
                mina = xd
        return mina
    
    def sizeoflargestcolumn(self):
        #do same like row after transpose
        p = self.df.transpose().tolist()
        maxa = 0
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd > maxa):
                maxa = xd
        return maxa

    def minsdcolumn(self):
        p1 = self.sizeofsmallestcolumn()
        p2 = self.size

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2
    
    def minmaxcolumn(self):
        p1 = self.sizeofsmallestcolumn()
        p2 = self.sizeoflargestcolumn()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2
    
    def diagonalmatrix(self):
        d = self.df
        count = 0 
        for i in range(self.size):
            if (d[i][i] > 0):
                count = count+ 1 
        return count
    
    def numberofcolumnsfilledcompletely(self):
        p = self.df.transpose().tolist()
        count = 0
        for x in p:
            xd = [i for i in x if i > 0]
            if (len(xd) == self.size):
                count += 1
        return count
    
    def numberofrowsfilledcompletely(self):
        p = self.df.tolist()
        count = 0
        for x in p:
            xd = [i for i in x if i > 0]
            if (len(xd) == self.size):
                count += 1

        return count
    
    def numberofrowsempty(self):
        p = self.df.tolist()
        count = 0
        for x in p:
            xd = [i for i in x if i == 0]
            if (len(xd) == self.size):
                count += 1

        return count
    
    def numberofcolumnsempty(self):
        p = self.df.transpose().tolist()
        count = 0
        for x in p:
            xd = [i for i in x if i == 0]
            if (len(xd) == self.size):
                count += 1
        return count
    
    def totalsumofnumbers(self): #standard deviation from sum, sum and total sum
        a = self.df.sum()
        su = 0
        for i in range(self.size):
            for j in range(1, (self.size +1)):
                su = su + j

        sd = a/su #standard deviation
        return a, sd

    def leastsubgridsum(self):
        a = self.getsubgrids()
        su = []
        for x in a:
            su.append(sum(x))    
        return min(su)

    def highestsubgridsum(self):
        a = self.getsubgrids()
        su = []
        for x in a:
            su.append(sum(x))
        return max(su)
    
    def leasthighestsubgrid(self):
        p1 = self.leastsubgridsum()
        p2 = self.highestsubgridsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2
    
    def leastmaxsubgrid(self):
        p1 = self.leastsubgridsum()
        p2 = self.sumof()
        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2 
    
    def highestmaxsubgrid(self):
        p1 = self.sumof()
        p2 = self.highestsubgridsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p2/p1

    def leastrowsum(self):
        a = self.df.tolist()
        su = [] 
        for x in a:
            su.append(sum(x))
        
        return min(su)

    def highestrowsum(self):
        a = self.df.tolist()
        su = [] 
        for x in a:
            su.append(sum(x))
        return max(su)
    
    def leasthighestrow(self):
        p1 = self.leastrowsum()
        p2 = self.highestrowsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2
    
    def leastmaxrow(self):
        p1 = self.leastrowsum()
        p2 = self.sumof()
        return p1/p2 
    
    def highestmaxrow(self):
        p1 = self.sumof()
        p2 = self.highestrowsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p2/p1
    
    def highestcolumnsum(self):        
        a = self.df.transpose().tolist()
        su = [] 
        for x in a:
            su.append(sum(x))
        return max(su)

    
    def leastcolumnsum(self):        
        a = self.df.transpose().tolist()
        su = [] 
        for x in a:
            su.append(sum(x))
        return min(su)

    def leasthighestcolumn(self):
        p1 = self.leastcolumnsum()
        p2 = self.highestcolumnsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2

    def leastmaxcolumn(self):
        p1 = self.leastcolumnsum()
        p2 = self.sumof()
        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2
    
    def highestmaxcolumn(self):
        p1 = self.sumof()
        p2 = self.highestcolumnsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p2/p1

    def highestoccurrenceofnumber(self):
        a = self.df
        s = a[a>0]
        #print(s.tolist())

        t = np.bincount(s)
        #print(t)
        if (t.size):
            return np.argmax(t)
        else: return 0
    
    #TODO: only one is being presented, not 2, same above
    def lowestoccurrenceofnumber(self):
        a = self.df
        s = a[a>0].tolist()
        if len(s):
            return min(s, key=s.count)
        else: return 0

    #Done
    def leastnumberforonesolution(self):
        """Contains atleast one less from the domain set of size!"""
        puzzle = self.df 
        a = np.unique(puzzle) 
        return len(a[a != 0])    
    
    #Done
    def least_condition_binary(self):
        if (self.leastnumberforonesolution() >= self.size-1):
            return 1
        else: return 0


    #Done
    def getmaxclique(self):
        x1 = self.sizeoflargestcolumn()
        x2 = self.sizeoflargestrow()
        x3 = self.sizeoflargestsubgrid()

        return max(x1,x2,x3)
    #TODO: see helper below
    def calculateedgesnumber(self):
        puzzle = self.df
        count =0
        for i in range(self.size):
            for j in range(self.size):
                if(puzzle[i][j] > 0 ):
                    count = self.helperforedges(i,j,count)
        return count/2
    #TODO : use graph class and adjacency matrix
    #us this also to calculate the max degree
    def helperforedges(self,i,j, count):
        #go through the entire row
        for k in range(self.size):
            if (self.df[i][k] > 0):
                count +=1
        #go through the entire column
        for l in range(self.size):
            if (self.df[l][j] > 0):
                count +=1
        #go through the entire subgrid
        return count 


    def deeplearning1(self):
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
        self.list_deepLearning.append(self.name_)
        for i in range(self.size):
            for j in range(self.size):
                self.list_deepLearning.append(self.df[i][j])
        return self.list_deepLearning
    
