from subprocess import call
def method_iter():
    for i in range(5,7): 
        for j in range(56,65,1): 
            for k in range(1,21):
                f = open("data/hard_puzzles/benchmarks%dx%d/%d/ortool%d.txt" %(i,i,j,k),"a+")
                call(["python3", "main.py", "hard_puzzles/benchmarks%dx%d/%d/puzzle%d" %(i,i,j,k), "cpsat"], stdout=f)
method_iter()