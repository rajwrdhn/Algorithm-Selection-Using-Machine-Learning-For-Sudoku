#!usr/var/python3
import math
import numpy as np
from scipy import stats

class feature_computations():
    """ This class computes features related to the 
        partial sudoku board and its attributes corresponding 
        to the sudoku board. """
    def __init__(self, df_np, size, name_l):
        self.df_np = df_np
        self.size = size
        self.list_deepLearning: list = []
        self.name_ = name_l
        self.order = int(math.sqrt(size))

    # size of the puzzle N
    def sizeofpuzzle(self):
        return int(self.size)
    
    # Order of the puzzle root(N)
    def orderofpuzzle(self):
        a = math.sqrt(self.size)
        return int(a)
    
    # total sum of domain of the board
    def sumof(self):
        k = self.size * (self.size + 1)       
        return int(k/2)
    
    # percent of filled cells
    # check with probability of filled cells
    def percentofnumbers(self):
        counter = 0
        for i in range(self.size):
            for j in range(self.size):
                if (self.df_np[i][j] > 0):
                    counter += 1 
        if (counter >0 ):
            per = counter * 100/ (self.size* self.size)
        else:
            per = 0  
        return per

    # mean/average of puzzle w.r.t. sum 
    def meanofpuzzle(self):
        a = np.mean(self.df_np)
        return a 

    # This is not required, mean has been done.
    def averageofpuzzle(self):
        a = np.average(self.df_np)
        return a 

    # Sum of all the numbers in the puzzle
    def sumofnumbers(self):
        s = np.sum(self.df_np)
        return int(s)

    # not needed at the moment
    def percentilepuzzle(self):
        p = np.percentile(self.df_np, 80)
        return p
    
    # Not used
    def calculate_points(self):
        li = self.df_np.tolist()
        return li
    
    # subgrids helper
    def getsubgrids(self):
        d = self.df_np#.tolist()
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
        return int(mina)

    # largest subgrid size wrt number of elements from the domain
    def sizeoflargestsubgrid(self):        
        p = self.getsubgrids()
        maxa = 0
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd > maxa):
                maxa = xd
        return int(maxa)
    

    # min isto max ratio subgrid size
    def minmaxsubgrid(self):
        p1 = self.sizeofsmallestsubgrid()
        p2 = self.sizeoflargestsubgrid()
        if p1==0 or p2==0:
            return 0
        else: return p1/p2
    
    # min isto max range subgrid size
    def rangeminmaxsubgrid(self):
        p1 = self.sizeofsmallestsubgrid()
        p2 = self.sizeoflargestsubgrid()
        return int(p2-p1)
    
    # min vs total range for subgrid
    def rangemintotalsubgrid(self):
        p1 = self.sizeoflargestsubgrid()
        p2 = self.size
        return int(p2-p1)
    
    # ratio of min from fullsize
    def minratiosubgrid(self):
        p1 = self.sizeofsmallestsubgrid()
        p2 = self.size

        if (p1 ==0):
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
        return int(count)
    
    # completely empty subgrids
    def numberofsubgridsempty(self):
        p = self.getsubgrids()
        count = 0
        for x in p:
            xd = [i for i in x if i==0]
            if (len(xd)==self.size):
                count += 1
        return int(count) 

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
        p = self.df_np.tolist()
        mina = self.size
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd < mina):
                mina = xd
        return int(mina)
    
    # largest row size
    def sizeoflargestrow(self):
        p = self.df_np.tolist()
        maxa = 0
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd > maxa):
                maxa = xd
        return int(maxa) 
    
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
        p = self.df_np.tolist()
        a = []
        for x in p:
            xd  = [i for i in x if i > 0]
            a.append(len(xd))
        sd = stats.tstd(a)
        return sd

    # size of the smallest column
    def sizeofsmallestcolumn(self):
        #do same like row after transpose
        p = self.df_np.transpose().tolist()
        mina = self.size
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd < mina):
                mina = xd
        return int(mina)
    
    # largest column size
    def sizeoflargestcolumn(self):
        #do same like row after transpose
        p = self.df_np.transpose().tolist()
        maxa = 0
        for x in p:
            xd = sum(i > 0 for i in x)
            if (xd > maxa):
                maxa = xd
        return int(maxa)

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
        p = self.df_np.transpose().tolist()
        a = []
        for x in p:
            xd  = [i for i in x if i > 0]
            a.append(len(xd))
        sd = stats.tstd(a)
        return sd
    
    # Return True if all diagonals are filled 
    def diagonalmatrix(self):
        d = self.df_np
        count = 0 
        for i in range(self.size):
            if (d[i][i] > 0):
                count = count+ 1         
        if count == self.size: return int(count),1
        else: return int(count), 0
    
    # Number of columns completely filled
    def numberofcolumnsfilledcompletely(self):
        p = self.df_np.transpose().tolist()
        count = 0
        for x in p:
            xd = [i for i in x if i > 0]
            if (len(xd) == self.size):
                count += 1
        return int(count)
    
    # Number of rows completely filled
    def numberofrowsfilledcompletely(self):
        p = self.df_np.tolist()
        count = 0
        for x in p:
            xd = [i for i in x if i > 0]
            if (len(xd) == self.size):
                count += 1

        return int(count)
    
    # number of empty rows
    def numberofrowsempty(self):
        p = self.df_np.tolist()
        count = 0
        for x in p:
            xd = [i for i in x if i == 0]
            if (len(xd) == self.size):
                count += 1

        return int(count)
    
    # number of empty columns
    def numberofcolumnsempty(self):
        p = self.df_np.transpose().tolist()
        count = 0
        for x in p:
            xd = [i for i in x if i == 0]
            if (len(xd) == self.size):
                count += 1
        return int(count)
    
    # sum of numbers on the sudoku board ratio and range
    #TODO in the main
    def totalsumofnumbersrr(self): #ratio and range from sum, sum and total sum
        a = self.df_np.sum()
        su = 0
        for i in range(self.size):
            for j in range(1, (self.size +1)):
                su = su + j

        r = su - a #range
        ra = a/su #ratio
        return int(r), ra

    # subgrid sum least
    def leastsubgridsum(self):
        a = self.getsubgrids()
        su = []
        for x in a:
            su.append(sum(x))    
        return int(min(su))

    # highest sum of subgrid
    def highestsubgridsum(self):
        a = self.getsubgrids()
        su = []
        for x in a:
            su.append(sum(x))
        return int(max(su))
    
    # least to highest ratio
    def leasthighestsubgrid(self):
        p1 = self.leastsubgridsum()
        p2 = self.highestsubgridsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2
    
    # least to max ratio
    def leastmaxsubgrid(self):
        p1 = self.leastsubgridsum()
        p2 = self.sumof()
        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2 
    
    # highest to max ratio
    def highestmaxsubgrid(self):
        p1 = self.sumof()
        p2 = self.highestsubgridsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p2/p1

    # least sum of the row
    def leastrowsum(self):
        a = self.df_np.tolist()
        su = [] 
        for x in a:
            su.append(sum(x))
        
        return int(min(su))

    # highest sum of the rows
    def highestrowsum(self):
        a = self.df_np.tolist()
        su = [] 
        for x in a:
            su.append(sum(x))
        return int(max(su))
    
    # least highest ratio
    def leasthighestrow(self):
        p1 = self.leastrowsum()
        p2 = self.highestrowsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2
    
    # least isto max ratio
    def leastmaxrow(self):
        p1 = self.leastrowsum()
        p2 = self.sumof()
        return p1/p2 
    
    # highest isto max row ratio
    def highestmaxrow(self):
        p1 = self.sumof()
        p2 = self.highestrowsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p2/p1
    
    # highest sum of columns
    def highestcolumnsum(self):        
        a = self.df_np.transpose().tolist()
        su = [] 
        for x in a:
            su.append(sum(x))
        return int(max(su))

    # least column sum
    def leastcolumnsum(self):        
        a = self.df_np.transpose().tolist()
        su = [] 
        for x in a:
            su.append(sum(x))
        return int(min(su))

    # least isto highest ratio column sum
    def leasthighestcolumn(self):
        p1 = self.leastcolumnsum()
        p2 = self.highestcolumnsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2

    # least isto max sum ratio column sum
    def leastmaxcolumn(self):
        p1 = self.leastcolumnsum()
        p2 = self.sumof()
        if (p1 ==0 or p2 ==0):
            return 0
        else: return p1/p2
    
    # highest isto max sum ratio column sum
    def highestmaxcolumn(self):
        p1 = self.sumof()
        p2 = self.highestcolumnsum()

        if (p1 ==0 or p2 ==0):
            return 0
        else: return p2/p1

    # max of multiplication of row
    def multiplymaxrow(self):
        a = self.df_np.tolist()
        m = []
        for x in a:
            m.append(self.listmul(x)) 
        return int(max(m))

    # helper for multiplication 
    def listmul(self, x):
        res = 1
        k = all(element == x[0] for element in x)
        if k:
            return 0
        else:             
            for a in x:
                if (a > 0):
                    res = res * a
        return res

    # max of multiplication of column
    def multiplymaxcolumn(self):
        a = self.df_np.transpose().tolist()
        m = []
        for x in a:
            m.append(self.listmul(x)) 
        return int(max(m))
    
    # max of multiplication of subgrid
    def multiplymaxsubgrid(self):
        a = self.getsubgrids()
        m =[]
        for x in a:
            m.append(self.listmul(x))
        return int(max(m))
    
    # min multiplication of row
    def multiplyminrow(self):
        a = self.df_np.tolist()
        m = []
        for x in a:
            m.append(self.listmul(x))
        return min(m)
    
    # min multiplication of column
    def multiplymincolumn(self):
        a = self.df_np.transpose().tolist()
        m = []
        for x in a:
            m.append(self.listmul(x))  
        return int(min(m))
    
    # min multiplication of subgrid
    def multiplyminsubgrid(self):
        a = self.getsubgrids() 
        m = []
        for x in a:
            m.append(self.listmul(x))
        return int(min(m))
    
    # range max to min row
    def rangemultiplyminmaxrow(self):
        m = self.multiplymaxrow() - self.multiplyminrow() 
        return int(m)  
    
    # range max to min column
    def rangemultiplyminmaxcolumn(self):
        m = self.multiplymaxcolumn() - self.multiplymincolumn() 
        return int(m)  
    
    # range max min subgrid
    def rangemultiplyminmaxsubgrid(self):
        m = self.multiplymaxsubgrid() - self.multiplyminsubgrid() 
        return int(m) 

    # store multiplication of each row as a list for sd
    def rowmultiplicationlist(self):
        r = self.df_np.tolist() # row
        mr = []
        for x in r:
            mr.append(self.listmul(x))
        return mr

    # store multiplication of each column as a list for sd
    def columnmultiplicationlist(self):
        c = self.df_np.transpose().tolist()        
        mc = []
        for x in c:
            mc.append(self.listmul(x))

        return mc  

    # store multiplication of each subgrid as a list for sd
    def subgridmultiplicationlist(self):
        sg = self.getsubgrids()
        ms = []
        for x in sg:
            ms.append(self.listmul(x))
        return ms

    # sudoku board multiplication full size
    def multiplyof(self):
        res = 1 
        for i in range(self.size):
            res = res * (i+1)
        return int(res)  
    
    # sd for full board row multiply
    def sdrowmultiply(self):
        a = self.rowmultiplicationlist() # data for sd
        sd = self.standarddevofmul(a)
        return sd
    
    # sd for full board column multiply
    def sdcolumnmultiply(self):
        a = self.columnmultiplicationlist() # data for sd
        sd = self.standarddevofmul(a)
        return sd
    
    # sd from full board column multiply
    def sdsubgridmultiply(self):
        a = self.subgridmultiplicationlist() # data for sd
        print(a)
        sd = self.standarddevofmul(a)
        return sd

    # mode of the sudoku board can have many numbers
    # is it okay to use it?
    #TODO: figure out wether to use it or not.
    def highestoccurrenceofnumber(self):
        a = self.df_np
        s = a[a>0]
        #print(s.tolist())
        t = np.bincount(s)
        #print(t)
        if (t.size):
            return int(np.argmax(t))
        else: return 0
    
    #TODO: only one is being presented, not 2, same above
    def lowestoccurrenceofnumber(self):
        a = self.df_np
        s = a[a>0].tolist()
        if len(s):
            return int(min(s, key=s.count))
        else: return 0

    # helper for least condition for one solution
    def leastnumberforonesolution(self):
        """Contains atleast one less from the domain set of size!"""
        puzzle = self.df_np 
        a = np.unique(puzzle) 
        return len(a[a != 0])    
    
    # least condition for a single solution 
    # binary output discrete data
    def leastconditionbinary(self):
        if (self.leastnumberforonesolution() >= self.size-1):
            return 1
        else: return 0

    # Done max clique gcp of sudoku
    def getmaxclique(self):
        x1 = self.sizeoflargestcolumn()
        x2 = self.sizeoflargestrow()
        x3 = self.sizeoflargestsubgrid()

        return int(max(x1,x2,x3))
    
    # min clique gcp of sudoku
    def getminclique(self):
        x1 = self.sizeofsmallestcolumn()
        x2 = self.sizeofsmallestrow()
        x3 = self.sizeofsmallestsubgrid()

        return int(min(x1,x2,x3))

    # range total min clique
    def getrangeminclique(self):
        r = self.size - self.getminclique()
        return int(r) 
    
    # range of total to max clique
    def getrangemaxclique(self):
        r = self.size - self.getmaxclique()
        return int(r) 
    
    # range min max clique
    def getrangeminmaxclique(self):
        r = self.getmaxclique() - self.getminclique()
        return int(r)

    # clique ratio
    def ratiominmaxclique(self):
        r = self.getminclique() / self.getmaxclique() 
        return r
        
    #TODO: see helper below
    def calculateedgesnumber(self):
        puzzle = self.df_np
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
            if (self.df_np[i][k] > 0):
                count +=1
        #go through the entire column
        for l in range(self.size):
            if (self.df_np[l][j] > 0):
                count +=1
        #go through the entire subgrid
        return count 


    def deeplearning1(self):
        self.list_deepLearning.append(self.name_)
        for i in range(self.size):
            for j in range(self.size):
                 
                if (self.df_np[i][j] > 0):
                    #insert 1 into the column as feature
                    self.list_deepLearning.append(1)
                else: #insert 0 into the coilumn as feature
                    self.list_deepLearning.append(0)
        return self.list_deepLearning
    
    def deeplearning2(self):
        self.list_deepLearning.append(self.name_)
        for i in range(self.size):
            for j in range(self.size):
                self.list_deepLearning.append(self.df_np[i][j])
        return self.list_deepLearning
    
    def meanofmul(self):
        m = self.multiplyof()
        return m
    
    def varianceofmul(self, data):
        m = self.meanofmul()
        n = self.size
        deviations = [(x - m) ** 2 for x in data]    
        v = sum(deviations) / n
        return v

    def standarddevofmul(self, data):
        sd = math.sqrt(self.varianceofmul(data))
        return sd  
    
    def meanofadd(self):
        m = self.sumof()
        return m
    
    def varianceofadd(self, data):
        m = self.meanofadd()
        n = self.size
        deviations = [(x - m) ** 2 for x in data]    
        v = sum(deviations) / n
        return v

    def standarddevofadd(self, data):
        sd = math.sqrt(self.varianceofadd(data))
        return sd 
    
    # store addition of each row as a list for sd
    def rowadditionlist(self):
        r = self.df_np.tolist() # row
        mr = []
        for x in r:
            mr.append(self.listadd(x))
        return mr

    # store addition of each column as a list for sd
    def columnadditionlist(self):
        c = self.df_np.transpose().tolist()        
        mc = []
        for x in c:
            mc.append(self.listadd(x))

        return mc  

    # store addition of each subgrid as a list for sd
    def subgridadditionlist(self):
        sg = self.getsubgrids()
        ms = []
        for x in sg:
            ms.append(self.listadd(x))
        return ms
    
    # helper for additon
    def listadd(self, data):
        res = 0 
        for x in data:
            res = res + x
        return res
    
    def sdrowaddition(self):
        a = self.rowadditionlist()
        sd = self.standarddevofadd(a)
        return sd

    def sdcolumnaddition(self):
        a = self.columnadditionlist()
        sd = self.standarddevofadd(a)
        return sd

    def sdsubgridaddition(self):
        a = self.subgridadditionlist()
        sd = self.standarddevofadd(a)
        return sd
    
    # maximum frequency mode of the number present 
    # in the puzzle from the domain
    def maxofnumber(self):
        #print(self.df_np[self.df_np>0])
        a = self.df_np[self.df_np>0].tolist()
        b = max(a,key=a.count)
        c = self.occurence(a,b)
        return int(b), int(c)
    
    # minimum frquency mode of the number present 
    # in the puzzle from the domain
    def minofnumber(self):
        #print(self.df_np[self.df_np>0])
        a = self.df_np[self.df_np>0].tolist()
        b = min(a,key=a.count)
        c = self.occurence(a,b)
        return int(b), int(c)
    
    # occurence of a number in a list
    def occurence(self, lst,x):
        count=0
        for i in lst:
            if (i==x):
                count=count+1
        return int(count)
    
    #count the total number of edges for the full sudoku
    def totaledges(self):
        d = self.maxdegree()
        e = int(d*(self.size*self.size)/2)
        return int(e)
    
    #calculate the max degree in the full sudoku
    def maxdegree(self):
        n = self.order
        #(3n + 1)(n − 1)
        md = (3*n + 1)*(n-1)
        return int(md)

    # total numbers in the puzzle
    # number nodes for the partial graph
    def numnodes(self):
        counter = 0
        for i in range(self.size):
            for j in range(self.size):
                if (self.df_np[i][j] > 0):
                    counter += 1 
        
        return int(counter)
    
    # missing numbers from the puzzle
    def missingnodes(self):
        counter = 0
        for i in range(self.size):
            for j in range(self.size):
                if (self.df_np[i][j] == 0):
                    counter += 1

        return int(counter)
    
    # max total number of edges for partial sudoku graph
    def maxnumedges(self):
        ne = (self.maxdegree() * self.numnodes()/2)
        return int(ne)
    
    # max missing number of edges for partial sudoku graph
    def maxmissingnumedges(self):
        ne = (self.maxdegree() * self.missingnodes()/2)
        return math.ceil(ne)
    
    # max degree for partial sudoku graph

    # set cover yes or no 
    # when 0 then its not a cover
    def setcover(self):
        a = np.unique(self.df_np)
        b = len(a) - 1
        if b == self.size:
            return 1
        else:
            return 0

    # min exact cover
    # minimum number of disjoint sets that make up the whole domain


    # number of elements from the domain
    def numdomain(self):
        a = np.unique(self.df_np)
        b = len(a) - 1
        return int(b)
    
    # missing count of domain
    def missingdomain(self):
        a = self.size
        b = self.numdomain()
        return int(a-b)
    
    def interquartilerangeforsudoku(self):
        a = stats.iqr(self.df_np)
        return a

if __name__ == "__main__":
    hard = np.array([ (3, 2, 0, 0),
            (0, 0, 0, 0),
            (1, 3, 0, 0),
            ( 2, 4, 0, 1)])
    model = feature_computations(hard, 4, "")
    print(model.maxdegree())
    print(model.totaledges())
    print(model.setcover())
    print(model.numdomain())
    print(model.missingnodes())
    print(model.maxnumedges())
    print(model.numnodes())
    print(model.meanofpuzzle())
    print(model.averageofpuzzle())
    print(model.maxmissingnumedges())
    print(model.interquartilerangeforsudoku())
    print(model.highestoccurrenceofnumber())
    print(model.lowestoccurrenceofnumber())