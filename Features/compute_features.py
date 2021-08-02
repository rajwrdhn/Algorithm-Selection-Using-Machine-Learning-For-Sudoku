#!usr/var/python3
import os
import math
import numpy as np
import matplotlib
import pandas as pd 
from scipy import stats
import scipy
from scipy.spatial import distance
from statistics import stdev


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

    # size of the puzzle N
    def sizeofpuzzle(self):
        return self.size
    
    # Order of the puzzle root(N)
    def orderofpuzzle(self):
        a = math.sqrt(self.size)
        return a
    
    # total sum of domain of the board
    def sumof(self):
        k = self.size * (self.size + 1)       
        return k/2
    
    # percent of filled cells
    # check with probability of filled cells
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

    # mean/average of puzzle 
    def meanofpuzzle(self):
        a = np.mean(self.df)
        return a 

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
    
    # Not used
    def calculate_points(self):
        li = self.df.tolist()
        return li
    
    # subgrids helper
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
    
    # smallest subgrid size wrt number of elements from the domain
    def sizeofsmallestsubgrid(self):        
        p = self.getsubgrids()
        mina = self.size
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd < mina):
                mina = xd
        return mina

    # largest subgrid size wrt number of elements from the domain
    def sizeoflargestsubgrid(self):        
        p = self.getsubgrids()
        maxa = 0
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd > maxa):
                maxa = xd
        return maxa
    
    # min isto max range subgrid size
    def rangeminmaxsubgrid(self):
        p1 = self.sizeofsmallestsubgrid()
        p2 = self.sizeoflargestsubgrid()
        return p2-p1
    
    # max vs total range for subgrid
    def rangemintotalsubgrid(self):
        p1 = self.sizeoflargestsubgrid()
        p2 = self.size
        return p2-p1
    
    # ratio of min from fullsize
    def minratiosubgrid(self):
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

    # size subgrid standard deviation
    def sdsizesubgrid(self):
        l = self.getsubgrids()
        a = []
        for x in l:
            xd = [i for i in x if i > 0]
            a.append(len(xd))
        sd = stats.tstd(a)
        return sd

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
    
    # min to max ratio
    def minmaxrow(self):
        p1 = self.sizeofsmallestrow()
        p2 = self.sizeoflargestrow()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2 
    
    # min to size ratio
    def minratiorow(self):
        p1 = self.sizeofsmallestrow()
        p2 = self.size

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2 

    # max to size ratio
    def maxratiorow(self):
        p1 = self.sizeoflargestrow()
        p2 = self.size

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2
    
    # standard deviation of row size to sample space 
    # i.e. Domain Size
    def sdsizerow(self):
        p = self.df.tolist()
        a = []
        for x in p:
            xd  = [i for i in x if i > 0]
            a.append(len(xd))
        sd = stats.tstd(a)
        return sd

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
    def minratiocolumn(self):
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

    # standard deviation of column size to sample space 
    # i.e. Domain Size
    def sdsizecolumn(self):
        p = self.df.transpose().tolist()
        a = []
        for x in p:
            xd  = [i for i in x if i > 0]
            a.append(len(xd))
        sd = stats.tstd(a)
        return sd
    
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
        a = self.getsubgrids()
        m =[]
        for x in a:
            m.append(self.listmul(x))
        return max(m)
    
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
        a = self.getsubgrids() 
        m = []
        for x in a:
            m.append(self.listmul(x))
        return min(m)
    
    def rangemultiplyminmaxrow(self):
        m = self.multiplymaxrow() - self.multiplyminrow() 
        return m  
    
    def rangemultiplyminmaxcolumn(self):
        m = self.multiplymaxcolumn() - self.multiplymincolumn() 
        return m  
    
    def rangemultiplyminmaxsubgrid(self):
        m = self.multiplymaxsubgrid() - self.multiplyminsubgrid() 
        return m 

    # store multiplication of each row as a list for sd
    def rowmultiplicationlist(self):
        r = self.df.tolist() # row
        c = self.df.transpose().tolist()
        sg = self.getsubgrids()
        mr = []
        for x in r:
            mr.append(self.listmul(x))
        
        mc = []
        for x in c:
            mc.append(self.listmul(x))

        ms = []
        for x in sg:
            mc.append(self.listmul(x))
        return mr, mc, ms  
    
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

    #Done helper for least condition for one solution
    def leastnumberforonesolution(self):
        """Contains atleast one less from the domain set of size!"""
        puzzle = self.df 
        a = np.unique(puzzle) 
        return len(a[a != 0])    
    
    # Done least condition for a single solution
    def least_condition_binary(self):
        if (self.leastnumberforonesolution() >= self.size-1):
            return 1
        else: return 0




    # Done max clique gcp of sudoku
    def getmaxclique(self):
        x1 = self.sizeoflargestcolumn()
        x2 = self.sizeoflargestrow()
        x3 = self.sizeoflargestsubgrid()

        return max(x1,x2,x3)
    
    # min clique gcp of sudoku
    def getminclique(self):
        x1 = self.sizeofsmallestcolumn()
        x2 = self.sizeofsmallestrow()
        x3 = self.sizeofsmallestsubgrid()

        return min(x1,x2,x3)

    # Standard deviation of max clique
    def getsdclique(self):
        sd = self.getmaxclique()/self.size
        return sd 
    
    # standard deviation of min clique
    def getmincliquesd(self):
        sd = self.getminclique() / self.size
        return sd 

    # clique ratio
    def ratiominmaxclique(self):
        r = self.getminclique() / self.getmaxclique() 
        return r

    # range clique
    def rangeminmaxclique(self):
        r = self.getminclique() - self.getmaxclique() 
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


if __name__ == "__main__":
    hard = np.array([ (3, 2, 0, 0),
            (0, 0, 0, 0),
            (1, 3, 4, 0),
            ( 2, 4, 0, 1)])
    model = feature_computations(hard, 4, "")
    print(model.sdsizecolumn())