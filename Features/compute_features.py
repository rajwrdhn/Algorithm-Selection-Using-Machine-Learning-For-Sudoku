#!usr/var/python3
import os
import math
import numpy as np
import matplotlib
import pandas as pd 
from scipy import stats
import scipy
from scipy.spatial import distance


class feature_computations():
    """ This class computes features related to the 
        partial sudoku board and its attributes corresponding 
        to the sudoku board. """
    def __init__(self, df, size, name_l):
        self.df = df
        self.size = size
        self.list_deepLearning: list = []
        self.name_ = name_l
        self.order = int(math.sqrt(size))

    def sizeofpuzzle(self):
        return self.size
    
    def orderofpuzzle(self):
        a = math.sqrt(self.size)
        return a
    
    # sum of all domain
    def sumof(self):
        k = self.size * (self.size + 1)       
        return k/2
    
    # percent of filled cells
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
    # mean of puzzle
    def meanofpuzzle(self):
        a = np.mean(self.df)
        return a 
    
    def medianofpuzzle(self):
        print(self.df)
        k = np.where(np.array(self.df) > 0)        
        m = np.median(k)
        return m
    
    # not to be done this way
    def modeofpuzzle(self):
        a = self.df.ravel()
        m = stats.mode(a, axis =None)        
        return m

    # This is not required, mean has been done.
    def averageofpuzzle(self):
        a = np.average(self.df)
        return a 

    # Sum of all the numbers in the puzzle
    def sumofnumbers(self):
        s = np.sum(self.df)
        return s

    # not needed at the moment
    def percentilepuzzle(self):
        p = np.percentile(self.df, 80)
        return p
    
    # Not needed or proper
    def manhattandistance(self):
        k = np.zeros((self.size,self.size)).astype(int).ravel()
        a = self.df.ravel()
        b = np.where(a > 0.5, 1, 0)
        p = distance.cityblock(b, k)
        return p 
        
    def calculate_points(self):
        li = self.df.tolist()
        return li
    
    # get subgrids helper
    def getsubgrids(self):
        d = self.df#.tolist()
        subgrids = []
        for box_i in range(self.order):
            for box_j in range(self.order):
                subgrid = []
                for i in range(self.order):
                    for j in range(self.order):
                        subgrid.append(d[self.order*box_i + i][self.order*box_j + j])
                subgrids.append(subgrid)
        return subgrids 
    
    # smallest subgrid
    def sizeofsmallestsubgrid(self):        
        p = self.getsubgrids()
        mina = self.size
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd < mina):
                mina = xd
        return mina

    # largest subgrid 
    def sizeoflargestsubgrid(self):        
        p = self.getsubgrids()
        maxa = 0
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd > maxa):
                maxa = xd
        return maxa
    
    # min isto max subgrid size standard deviation
    def minmaxsubgrid(self):
        p1 = self.sizeofsmallestsubgrid()
        p2 = self.sizeoflargestsubgrid()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2
    
    # sd of min from fullsize
    def minsdsubgrid(self):
        p1 = self.sizeofsmallestsubgrid()
        p2 = self.size

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2

    # number of subgrids filled completely
    def numberofsubgridsfilledcompletely(self):
        p = self.getsubgrids()
        count = 0
        for x in p:
            xd = [i for i in x if i > 0]
            if (len(xd) == self.size):
                count += 1
        return count
    
    # completely empty subgrids
    def numberofsubgridsempty(self):
        p = self.getsubgrids()
        count = 0
        for x in p:
            xd = [i for i in x if i==0]
            if (len(xd)==self.size):
                count += 1
        return count 

    # smallest row size
    def sizeofsmallestrow(self):
        p = self.df.tolist()
        mina = self.size
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd < mina):
                mina = xd
        return mina
    
    # largest row size
    def sizeoflargestrow(self):
        p = self.df.tolist()
        maxa = 0
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd > maxa):
                maxa = xd
        return maxa 
    
    # min to max standard deviation
    def minmaxrow(self):
        p1 = self.sizeofsmallestrow()
        p2 = self.sizeoflargestrow()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2 
    
    # min to size standard deviation
    def minsdrow(self):
        p1 = self.sizeofsmallestrow()
        p2 = self.size

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2 

    # max to size standard deviation
    def maxsdrow(self):
        p1 = self.sizeoflargestrow()
        p2 = self.size

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2   
    
    # size of the smallest column
    def sizeofsmallestcolumn(self):
        #do same like row after transpose
        p = self.df.transpose().tolist()
        mina = self.size
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd < mina):
                mina = xd
        return mina
    
    # largest column size
    def sizeoflargestcolumn(self):
        #do same like row after transpose
        p = self.df.transpose().tolist()
        maxa = 0
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd > maxa):
                maxa = xd
        return maxa

    # standard deviation min column to size
    def minsdcolumn(self):
        p1 = self.sizeofsmallestcolumn()
        p2 = self.size

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2
    
    # standard deviation min to max
    def minmaxcolumn(self):
        p1 = self.sizeofsmallestcolumn()
        p2 = self.sizeoflargestcolumn()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2
    
    # Return True if all diagonals are filled 
    def diagonalmatrix(self):
        d = self.df
        count = 0 
        for i in range(self.size):
            if (d[i][i] > 0):
                count = count+ 1         
        return count == self.size
    
    # Number of columns completely filled
    def numberofcolumnsfilledcompletely(self):
        p = self.df.transpose().tolist()
        count = 0
        for x in p:
            xd = [i for i in x if i > 0]
            if (len(xd) == self.size):
                count += 1
        return count
    
    # Number of rows completely filled
    def numberofrowsfilledcompletely(self):
        p = self.df.tolist()
        count = 0
        for x in p:
            xd = [i for i in x if i > 0]
            if (len(xd) == self.size):
                count += 1

        return count
    
    # number of empty rows
    def numberofrowsempty(self):
        p = self.df.tolist()
        count = 0
        for x in p:
            xd = [i for i in x if i == 0]
            if (len(xd) == self.size):
                count += 1

        return count
    
    # number of empty columns
    def numberofcolumnsempty(self):
        p = self.df.transpose().tolist()
        count = 0
        for x in p:
            xd = [i for i in x if i == 0]
            if (len(xd) == self.size):
                count += 1
        return count
    
    # sum of numbers on the sudoku board standard deviation
    def totalsumofnumberssd(self): #standard deviation from sum, sum and total sum
        a = self.df.sum()
        su = 0
        for i in range(self.size):
            for j in range(1, (self.size +1)):
                su = su + j

        sd = a/su #standard deviation
        return sd

    # subgrid sum least
    def leastsubgridsum(self):
        a = self.getsubgrids()
        su = []
        for x in a:
            su.append(sum(x))    
        return min(su)

    # highest sum of subgrid
    def highestsubgridsum(self):
        a = self.getsubgrids()
        su = []
        for x in a:
            su.append(sum(x))
        return max(su)
    
    # least to highest sd 
    def leasthighestsubgrid(self):
        p1 = self.leastsubgridsum()
        p2 = self.highestsubgridsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2
    
    # least to max sd
    def leastmaxsubgrid(self):
        p1 = self.leastsubgridsum()
        p2 = self.sumof()
        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2 
    
    # highest to max sd
    def highestmaxsubgrid(self):
        p1 = self.sumof()
        p2 = self.highestsubgridsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p2/p1

    # least sum of the row
    def leastrowsum(self):
        a = self.df.tolist()
        su = [] 
        for x in a:
            su.append(sum(x))
        
        return min(su)

    # highest sum of the rows
    def highestrowsum(self):
        a = self.df.tolist()
        su = [] 
        for x in a:
            su.append(sum(x))
        return max(su)
    
    # least highest ratio
    def leasthighestrow(self):
        p1 = self.leastrowsum()
        p2 = self.highestrowsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2
    
    # least isto max sd
    def leastmaxrow(self):
        p1 = self.leastrowsum()
        p2 = self.sumof()
        return p1/p2 
    
    # highest isto max row
    def highestmaxrow(self):
        p1 = self.sumof()
        p2 = self.highestrowsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p2/p1
    
    # highest sum of columns
    def highestcolumnsum(self):        
        a = self.df.transpose().tolist()
        su = [] 
        for x in a:
            su.append(sum(x))
        return max(su)

    # least column sum
    def leastcolumnsum(self):        
        a = self.df.transpose().tolist()
        su = [] 
        for x in a:
            su.append(sum(x))
        return min(su)

    # least isto highest ratio column sum
    def leasthighestcolumn(self):
        p1 = self.leastcolumnsum()
        p2 = self.highestcolumnsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2

    # least isto max sum sd column sum
    def leastmaxcolumn(self):
        p1 = self.leastcolumnsum()
        p2 = self.sumof()
        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2
    # highest isto max sum sd column sum
    def highestmaxcolumn(self):
        p1 = self.sumof()
        p2 = self.highestcolumnsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p2/p1

    # max of multiplication of row
    def multiplymaxrow(self):
        a = self.df.tolist()
        m = []
        for x in a:
            m.append(self.listmul(x)) 
        return max(m)

    # helper for multiplication 
    def listmul(self, x):
        res = 1
        for a in x:
            if (a > 0):
                res = res * a
        return res

    # max of multiplication of column
    def multiplymaxcolumn(self):
        a = self.df.transpose().tolist()
        m = []
        for x in a:
            m.append(self.listmul(x)) 
        return max(m)
    
    def multiplymaxsubgrid(self):
        return 0 
    
    def multiplyminrow(self):
        a = self.df.tolist()
        m = []
        for x in a:
            m.append(self.listmul(x))
        return min(m)
    
    def multiplymincolumn(self):
        a = self.df.transpose().tolist()
        m = []
        for x in a:
            m.append(self.listmul(x))  
        return min(m)
    
    def multiplyminsubgrid(self):
        return 0
    
    def sdmultiplyminmaxrow(self):
        return 0
    
    def sdmultiplyminmaxcolumn(self):
        return 0
    
    def sdmultiplyminmaxsubgrid(self):
        return 0
    
    def sdminrowmultiply(self):
        return 0
    
    def sdmaxrowmultiply(self):
        return 0
    
    def sdmincolumnmultiply(self):
        return 0
    
    def sdmaxcolumnmultiply(self):
        return 0
    
    def sdminsubgridmultiply(self):
        return 0
    
    def sdmaxsubgridmultiply(self):
        return 0

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
    
    def getminclique(self):
        x1 = self.sizeofsmallestcolumn()
        x2 = self.sizeofsmallestrow()
        x3 = self.sizeofsmallestsubgrid()

        return min(x1,x2,x3)

    #Standard deviation of max clique
    def getsdclique(self):
        sd = self.getmaxclique()/self.size
        return sd 
    
    #standard deviation of min clique
    def getmincliquesd(self):
        sd = self.getminclique() / self.size
        return sd 

    def ratiominmaxclique(self):
        r = self.getminclique() / self.getmaxclique() 
        return r
        
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
    #use this also to calculate the max degree
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
