import pandas

def read_ortool_time():
    for i in range(6,7): 
        for j in range(0,105,5): 
            for k in range(1,21):
                f = open("data/benchmark_puzzles/benchmarks%dx%d/%d/ortool%d.txt" %(i,i,j,k),"r+")
                ortime = []
                lines = f.readlines()
                ortime.append(lines)
    pandas.DataFrame() 
    print (ortime)


read_ortool_time()


