#!usr/var/python3
import unittest
import compute_features
import numpy as np
class TestFeatureMethods(unittest.TestCase):
    def test_sumof(self):
        self.assertEqual(model.sumof(), 10)

    def test_percentofnumbers(self):       
        self.assertEqual(model.percentofnumbers(), 50)
    
    def test_meanofpuzzle(self):      
        self.assertEqual(model.meanofpuzzle(), 1.25)

    def test_sumofnumbers(self):        
        self.assertEqual(model.sumofnumbers(), 20)
    
    def test_getsubgrids(self):       
        self.assertEqual(model.getsubgrids(), 
            [[3, 2, 0, 0], [0, 0, 0, 0], 
            [1, 3, 2, 4], [4, 0, 0, 1]])

    def test_sizeofsmallestsubgrid(self):        
        self.assertEqual(model.sizeofsmallestsubgrid(), 0)
    
    def test_sizeoflargestsubgrid(self):       
        self.assertEqual(model.sizeoflargestsubgrid(), 4)
        
    def test_rangeminmaxsubgrid(self):
        self.assertEqual(model.rangeminmaxsubgrid(), 4)
    
    def test_minratiosubgrid(self):
        self.assertEqual(model.minratiosubgrid(), 0)
    
    def test_numberofsubgridsfilledcompletely(self):
        self.assertEqual(model.numberofsubgridsfilledcompletely(),1)
    
    def test_numberofsubgridsempty(self):
        self.assertEqual(model.numberofsubgridsempty(), 1)
    
    def test_sizeofsmallestrow(self):
        self.assertEqual(model.sizeofsmallestrow(),0)
    
    def test_sizeoflargestrow(self):
        self.assertEqual(model.sizeoflargestrow(), 3)
    
    def test_minmaxrow(self):
        self.assertEqual(model.minmaxrow(), 0)
    
    def test_minsdrow(self):
        self.assertEqual(model.minratiorow(), 0)
    
    def test_maxsdrow(self):
        self.assertEqual(model.maxratiorow(), 3/4)
    
    def test_sizeofsmallestcolumn(self):
        self.assertEqual(model.sizeofsmallestcolumn(), 1)

    def test_sizeoflargestcolumn(self):
        self.assertEqual(model.sizeoflargestcolumn(), 3)
    
    def test_minratiocolumn(self):
        self.assertEqual(model.minratiocolumn(), 1/4)
    
    def test_minmaxcolumn(self):
        self.assertEqual(model.minmaxcolumn(), 1/3)
    
    def test_diagonalmatrix(self):
        self.assertEqual(model.diagonalmatrix(), False)
    
    def test_numberofcolumnsfilledcompletely(self):
        self.assertEqual(model.numberofcolumnsfilledcompletely(), 0)

    def test_numberofrowsfilledcompletely(self):
        self.assertEqual(model.numberofrowsfilledcompletely(), 0)

    def test_numberofcolumnsempty(self):
        self.assertEqual(model.numberofcolumnsempty(), 0)

    def test_numberofrowsempty(self):
        self.assertEqual(model.numberofrowsempty(), 1)
    
    def test_totalpuzzlesumsd(self):
        self.assertEqual(model.totalsumofnumbersrr(), (20 , 20/40))
    
    def test_leastsubgridsum(self):
        self.assertEqual(model.leastsubgridsum(), 0)

    def test_highestsubgridsum(self):
        self.assertEqual(model.highestsubgridsum(), 10)
    
    def test_leasthighestsubgrid(self):
        self.assertEqual(model.leasthighestsubgrid(), 0)
    
    def test_leastmaxsubgrid(self):
        self.assertEqual(model.leastmaxsubgrid(), 0)
    
    def test_highestmaxsubgrd(self):
        self.assertEqual(model.highestmaxsubgrid(), 1)
    
    def test_leastrowsum(self):
        self.assertEqual(model.leastrowsum(), 0)

    def test_highestrowsum(self):
        self.assertEqual(model.highestrowsum(), 8)
    
    def test_leasthighestrowratio(self):
        self.assertEqual(model.leasthighestrow(), 0)
    
    def test_leastmaxrow(self):
        self.assertEqual(model.leastmaxrow(), 0)

    def test_highestmaxrow(self):
        self.assertEqual(model.highestmaxrow(), 8/10)
    
    def test_highestcolumnsum(self):
        self.assertEqual(model.highestcolumnsum(), 9)
    
    def test_leastcolumnsum(self):
        self.assertEqual(model.leastcolumnsum(), 1)
    
    def test_leasthighestcolumn(self):
        self.assertEqual(model.leasthighestcolumn(), 1/9)

    def test_leastmaxcolumn(self):
        self.assertEqual(model.leastmaxcolumn(), 1/10)

    def test_highestmaxcolumn(self):
        self.assertEqual(model.highestmaxcolumn(), 9/10)
    
    def test_multiplymaxrow(self):
        self.assertEqual(model.multiplymaxrow(), 12)

    def test_multiplymaxcolumn(self):
        self.assertEqual(model.multiplymaxcolumn(), 24)

    def test_multiplyminrow(self):
        self.assertEqual(model.multiplyminrow(), 0)

    def test_multiplymincolumn(self):
        self.assertEqual(model.multiplymincolumn(),1)

if __name__ == '__main__':
    hard = np.array([ (3, 2, 0, 0),
            (0, 0, 0, 0),
            (1, 3, 4, 0),
            ( 2, 4, 0, 1)])
    model = compute_features.feature_computations(hard, 4, "")
    unittest.main()