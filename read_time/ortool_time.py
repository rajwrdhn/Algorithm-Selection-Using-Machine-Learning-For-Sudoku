import os.path

def method_iter():
    lis_or = []
    for i in range(3,8): 
        for j in range(0,105,5): 
            for k in range(1,21):
                if os.path.exists("/home/raj/Music/SudokuSolvers/Python/data/benchmark_puzzles/benchmarks%dx%d/%d/ortool%d.txt" %(i,i,j,k)):
                    f = open("/home/raj/Music/SudokuSolvers/Python/data/benchmark_puzzles/benchmarks%dx%d/%d/ortool%d.txt" %(i,i,j,k),"r")
                    print(f.readlines())
                else:
                    print("check me")
                    continue

                    
method_iter()