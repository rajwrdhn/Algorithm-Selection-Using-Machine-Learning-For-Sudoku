#FlatZinc features

import os.path
import pandas
dict_chuf: list = [[]]
dict_gurobi: list = [[]]
dict_cplex: list = [[]]
def method_iter():
    lis_or = []
    for i in range(3,10): 
        for j in range(0,105,5): 
            for k in range(1,21):
                
                if os.path.exists("/home/raj/Music/MiniZincIDE-2.4.3-bundle-linux-x86_64/bin/benchmark_puzzles/benchmarks%dx%d/%d/chuf%d.dzn" %(i,i,j,k)):
                    f = open("/home/raj/Music/MiniZincIDE-2.4.3-bundle-linux-x86_64/bin/benchmark_puzzles/benchmarks%dx%d/%d/chuf%d.dzn" %(i,i,j,k),"r")
                    a = f.readlines()
                    try:
                        dict_chuf.append(["benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(i,i,j,k), float(a[1][19:-1]), float(a[2][25:-1]),float(a[3][32:-1]),float(a[5][22:-1])]) 
                    except:
                        pass
                if os.path.exists("/home/raj/Music/MiniZincIDE-2.4.3-bundle-linux-x86_64/bin/benchmark_puzzles/benchmarks%dx%d/%d/gurobi%d.dzn" %(i,i,j,k)):
                    f = open("/home/raj/Music/MiniZincIDE-2.4.3-bundle-linux-x86_64/bin/benchmark_puzzles/benchmarks%dx%d/%d/gurobi%d.dzn" %(i,i,j,k),"r")
                    a = f.readlines()
                    try:
                        dict_gurobi.append(["benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(i,i,j,k), float(a[1][19:-1]), float(a[2][25:-1]),float(a[3][32:-1]),float(a[5][22:-1])])
                    except:
                        pass
                if os.path.exists("/home/raj/Music/MiniZincIDE-2.4.3-bundle-linux-x86_64/bin/benchmark_puzzles/benchmarks%dx%d/%d/cplex%d.dzn" %(i,i,j,k)):
                    f = open("/home/raj/Music/MiniZincIDE-2.4.3-bundle-linux-x86_64/bin/benchmark_puzzles/benchmarks%dx%d/%d/cplex%d.dzn" %(i,i,j,k),"r")
                    a = f.readlines()
                    try:
                        dict_cplex.append(["benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(i,i,j,k), float(a[1][19:-1]), float(a[2][25:-1]),float(a[3][32:-1]),float(a[5][22:-1])])
                    except:
                        pass
method_iter()
df = pandas.DataFrame(dict_chuf, columns=['name', 'pathschuf', 'flatintvarschuf','flatintconstraintschuf','flattimechuf'])
df[1:].to_csv('/home/raj/Music/SudokuSolvers/read_time/chuffeature.csv',index=False)

df = pandas.DataFrame(dict_gurobi, columns=['name','pathsgurobi', 'flatintvarsgurobi','flatintconstraintsgurobi','flattimegurobi'])
df[1:].to_csv('/home/raj/Music/SudokuSolvers/read_time/gurobifeature.csv',index=False)

df = pandas.DataFrame(dict_cplex, columns=['name','pathscplex', 'flatintvarscplex','flatintconstraintscplex','flattimecplex'])
df[1:].to_csv('/home/raj/Music/SudokuSolvers/read_time/cplexfeature.csv',index=False)