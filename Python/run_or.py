from subprocess import call
def method_iter():
    for i in range(6,7): 
        for j in range(0,105,5): 
            for k in range(1,21):
                f = open("data/benchmark_puzzles/benchmarks%dx%d/%d/cpsat%d.txt" %(i,i,j,k),"a+")
                call(["python3", "main.py", "benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d" %(i,i,j,k), "cpsat"], stdout=f)
method_iter()