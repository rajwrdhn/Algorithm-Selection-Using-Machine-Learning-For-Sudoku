#!usr/var/python3
import unittest
import compute_features
hard = [[3, 2, 0, 0],
            [0, 0, 0, 0],
            [1, 3, 4, 0],
            [0, 0, 0, 1]]
class TestFeatureMethods(unittest.TestCase):
    def test_sumof(self):
        model = compute_features.feature_computations(hard, 4, "")
        self.assertEqual(model.sumof(), 10)

    def test_percentofnumbers(self):
        model = compute_features.feature_computations(hard, 4, "")
        self.assertEqual(model.percentofnumbers(), 600/16)
    
    def test_meanofpuzzle(self):
        model = compute_features.feature_computations(hard, 4, "")
        self.assertEqual(model.meanofpuzzle(), 14/16)
    
    def test_medianofpuzzle(self):
        model = compute_features.feature_computations(hard, 4, "")
        #self.assertEqual(model.medianofpuzzle(),2.5)
    
    def test_sumofnumbers(self):
        model = compute_features.feature_computations(hard, 4, "")
        self.assertEqual(model.sumofnumbers(), 14)


if __name__ == '__main__':
    unittest.main()