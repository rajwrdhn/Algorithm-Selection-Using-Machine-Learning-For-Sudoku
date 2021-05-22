import os.path
import re
import pandas
dict_hls: list = [[]]
def method_iter():
    lis_or = []
    for i in range(3,10): 
        for j in range(0,105,5): 
            for k in range(1,21):
                if os.path.exists("/home/raj/Music/Thesis/sudokusolver_sources/build/data/benchmark_puzzles/benchmarks%dx%d/%d/HybridILS%d_log.txt" %(i,i,j,k)):
                    f = open("/home/raj/Music/Thesis/sudokusolver_sources/build/data/benchmark_puzzles/benchmarks%dx%d/%d/HybridILS%d_log.txt" %(i,i,j,k),"r")
                    a = f.readlines()
                    #print("benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(i,i,j,k), a)
                    for x in a:
                        if (x[0:1] != '0'):
                            name_l = "benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(i,i,j,k)
                            if (x[0:1] == '1'):
                                dict_hls.append([name_l, int(x[2:-1])/1000, 'Hybrid'])
                            else:
                                continue
                        else:
                            continue
                    #print(dict_hls)
                else:
                    #print("benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(i,i,j,k), "check me")
                    continue

                    
method_iter()
df = pandas.DataFrame(dict_hls, columns=['name', 'time', 'algo'])
df[1:].to_csv('/home/raj/Music/SudokuSolvers/read_time/hy_ls.csv',index=False)
