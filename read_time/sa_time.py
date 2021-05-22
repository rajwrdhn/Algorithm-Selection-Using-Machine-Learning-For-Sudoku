import os.path
import re
import pandas
from pandas import DataFrame
list_sa: list = [[]]
#list_sa.append('name', 'time', 'algo')
def method_iter():
    for i in range(3,10): 
        for j in range(0,105,5): 
            for k in range(1,21):
                if os.path.exists("/home/raj/Music/OtherSolvers/sudokuSolverMetaheuristics/PublicVersionOfCode/data/benchmark_puzzles/benchmarks%dx%d/%d/sa_log_%d.txt" %(i,i,j,k)):
                    f = open("/home/raj/Music/OtherSolvers/sudokuSolverMetaheuristics/PublicVersionOfCode/data/benchmark_puzzles/benchmarks%dx%d/%d/sa_log_%d.txt" %(i,i,j,k),"r")
                    f1 = open("/home/raj/Music/OtherSolvers/sudokuSolverMetaheuristics/PublicVersionOfCode/data/benchmark_puzzles/benchmarks%dx%d/%d/sa_time_%d.txt" %(i,i,j,k),"r")
                    a = f.readlines()
                    a1 = f1.readlines()
                    #print("benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(i,i,j,k), a)
                    for x in a:
                        if (x[0:1] == '0'):
                            name_l = "benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(i,i,j,k)
                            for x1 in a1:
                                if (x1 != '0'):
                                    list_sa.append([name_l, float(x1[:-1]), 'SA'])
                                    
                                else:
                                    continue
                        else:
                            continue
                    #print(df)
                    #df = DataFrame (list_sa).transpose()

                else:
                    #print("benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(i,i,j,k), "check me")
                    continue

                    
method_iter()
df = pandas.DataFrame(list_sa, columns=['name', 'time', 'algo'])
df[1:].to_csv('/home/raj/Music/SudokuSolvers/read_time/satime.csv',index=False)
#print(df)