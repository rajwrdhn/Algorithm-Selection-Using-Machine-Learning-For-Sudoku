
def method_get():
    for i in range(6,7): 
        for j in range(90,105,5): 
            for k in range(1,21):
                f = open("data/benchmark_puzzles/benchmarks%dx%d/%d/cpsat%d.txt" %(i,i,j,k),"r")
                
method_get()