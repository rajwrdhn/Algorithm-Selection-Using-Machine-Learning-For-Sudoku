mport sys
from subprocess import call
from subprocess import Popen, PIPE
import Solver_cpsat
#import pandas
def method_iter():
    for i in range(6,10): 
        for j in range(95,105,5): 
            for k in range(1,21):
                #call(["./minizinc","-s --solver chuffed","sudoku.mzn","benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.dzn" %(i,i,j,k)])
                
                #print("./minizinc", "-s","--solver","sudoku.mzn")
                f = open("data/benchmark_puzzles/benchmarks%dx%d/%d/cpsat%d.txt" %(i,i,j,k),"a+")
                call(["./minizinc", "-s", "--solver", "chuffed", "sudoku.mzn", "benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.dzn" %(i,i,j,k)], stdout=f)

                #pandas.to_csv("")
method_iter()