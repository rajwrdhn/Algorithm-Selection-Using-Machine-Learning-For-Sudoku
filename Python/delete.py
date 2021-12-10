import os

def method_iter():
    for i in range(3,10): 
        for j in range(0,105,5): 
            for k in range(1,21):
                f = "/home/raj/Videos/data/benchmark_puzzles/benchmarks%dx%d/%d/cpsat%d.txt" %(i,i,j,k)
                f1 = "/home/raj/Videos/data/benchmark_puzzles/benchmarks%dx%d/%d/puzzle0.txt" %(i,i,j)
                if os.path.isfile(f):
                    print(f)
                    os.remove(f)

                if os.path.exists(f1):
                    print(f1)
                    os.remove(f1)
method_iter()