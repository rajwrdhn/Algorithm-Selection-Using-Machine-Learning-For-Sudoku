#!usr/bin/python3
import os
import numpy as np
import pandas as pd 
from scipy import stats
import scipy
from scipy.spatial import distance

class convert_puzzle_to_matrix():
    def __init__(self, a):
        self.a = a 