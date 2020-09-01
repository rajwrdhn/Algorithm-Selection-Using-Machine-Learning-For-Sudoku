from subprocess import call
def method_iter():
    for i in range(7,8): 
        for j in range(80,85,5): 
            for k in range(14,21):
                f = open("data/benchmark_puzzles/benchmarks%dx%d/%d/ortool%d.txt" %(i,i,j,k),"a+")
                call(["python3", "main.py", "benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d" %(i,i,j,k), "cpsat"], stdout=f)
method_iter()