import os.path
import pandas
lis_or: list = [[]]
def method_iter():

    for i in range(3,10): 
        for j in range(5,100,5): 
            for k in range(1,21,1):
                if os.path.exists("/home/raj/Music/SudokuSolvers/Python/data/benchmark_puzzles/benchmarks%dx%d/%d/ortool%d.txt" %(i,i,j,k)):
                    f = open("/home/raj/Music/SudokuSolvers/Python/data/benchmark_puzzles/benchmarks%dx%d/%d/ortool%d.txt" %(i,i,j,k),"r")
                    a = f.readlines()
                    #print("benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(i,i,j,k), a)
                    #if ()
                    for x in a:
                        if (x == 'solved\n'):
                            name_l = "benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(i,i,j,k)
                            if 'solved\n' in a[0]:
                                lis_or.append([name_l, float(a[1]),'or']) 
                            elif 'solved\n' in a[2]:
                                lis_or.append([name_l, float(a[3]),'or'])
                            elif 'solved\n' in a[4]:
                                lis_or.append([name_l, float(a[5]),'or'])
                            else:
                                continue
                        else:
                            continue
                    #print(lis_or)
                else:
                    #print("benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(i,i,j,k), "check me")
                    continue
                    
method_iter()
df = pandas.DataFrame(lis_or, columns=['name', 'time', 'algo'])
d = df[df.time <= 3600].groupby('name').mean()
d.to_csv('/home/raj/Music/SudokuSolvers/read_time/or/ortime.csv',index=True)
#print(df[df.time <= 3600].groupby('name').mean().describe())
print(d)