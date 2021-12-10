import pandas as pd 


df1 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/chuffed/chuffeature.csv")
df2 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/chuffed/chuftime.csv")
print(df1)
print(df2)
d = pd.merge(df1,df2)
d['comtime'] = d['flattimechuf'] + d['time']
#d.to_csv("/home/raj/Music/SudokuSolvers/read_time/chuffed/chtime.csv")
print(d)
df3 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/cplex/cplexfeature.csv")
df4 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/cplex/cplextime.csv")
b = pd.merge(df3,df4)
b['comtime'] = b['flattimecplex'] + b['time']
#b.to_csv("/home/raj/Music/SudokuSolvers/read_time/cplex/cptime.csv")
print(b)
df5 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/gurobi/gurobifeature.csv")
df6 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/gurobi/gurobitime.csv")
c = pd.merge(df5,df6)
c['comtime'] = c['flattimegurobi'] + c['time']
#c.to_csv("/home/raj/Music/SudokuSolvers/read_time/gurobi/gutime.csv")
print(c)