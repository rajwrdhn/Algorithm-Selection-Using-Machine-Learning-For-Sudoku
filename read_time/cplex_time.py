import os.path
import pandas
dict_plex: list = [[]]
def method_iter():
    lis_or = []
    for i in range(3,10): 
        for j in range(0,105,5): 
            for k in range(1,21):
                if os.path.exists("/home/raj/Music/MiniZincIDE-2.4.3-bundle-linux-x86_64/bin/benchmark_puzzles/benchmarks%dx%d/%d/cplex%d.dzn" %(i,i,j,k)):
                    f = open("/home/raj/Music/MiniZincIDE-2.4.3-bundle-linux-x86_64/bin/benchmark_puzzles/benchmarks%dx%d/%d/cplex%d.dzn" %(i,i,j,k),"r")
                    a = f.readlines()
                    for x in a:
                        if (x[:17]== '=====UNKNOWN====='):
                            break
                        else:
                            if (x[:22]== '%%%mzn-stat solveTime='):
                                #print("hi")

                                dict_plex.append(["benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(i,i,j,k), float(x[22:-1]),'cplex'])
                                #print("benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(i,i,j,k), x)
                            else:
                                continue
                else:
                    #print("benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(i,i,j,k), "check me")
                    continue

                    
method_iter()
df = pandas.DataFrame(dict_plex, columns=['name', 'time', 'algo'])
df[1:].to_csv('/home/raj/Music/SudokuSolvers/read_time/cplex.csv',index=False)
#print(df)