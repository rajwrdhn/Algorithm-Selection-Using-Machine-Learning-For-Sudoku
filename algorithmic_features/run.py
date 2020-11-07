from subprocess import call
def method_iter():
    for i in range(3,8): 
        for j in range(0,105,5): 
            for k in range(1,21):
                f = open("data/benchmark_puzzles/benchmarks%dx%d/%d/ortool%d.txt" %(i,i,j,k),"r")
                call(["python3", "read_sudoku_puzzles.py", "benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d" %(i,i,j,k), "GET"], stdin=f)
method_iter()