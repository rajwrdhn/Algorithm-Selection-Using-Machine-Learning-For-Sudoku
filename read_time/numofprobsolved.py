
import pandas as pd 


df1 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/sa/satime.csv", )
df1['algo'] = 'sima'
df1['comtime'] = df1['time']
#print(df1)

df2 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/or/ortime.csv")
df2['algo'] = 'ortl'
df2['comtime'] = df2['time']
#print(df2)

df3 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/chuffed/chuftime.csv")
df3['algo'] = 'chuf'
#print(df3)

df4 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/cplex/cplextime.csv")
df4['algo'] = 'cplex'
#print(df4)

df5 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/gurobi/gurobitime.csv")
df5['algo'] = 'gurobi'
#print(df5)

df6 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/hybrid/hyilstime.csv")
df6['algo'] = 'hyils'
df6['comtime'] = df6['time']
#print(df6)


df7 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/chuffed/chtime.csv")
df8 = df3.merge(df7)
df9 = df8[['name','comtime','algo']]

df10 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/cplex/cptime.csv")
df11 = df4.merge(df10)
df12 = df11[['name','comtime','algo']]

df13 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/gurobi/gutime.csv")
df14 = df5.merge(df13)
df15 = df14[['name','comtime','algo']]

#kf = pd.concat([df1,df2,df6,df9,df12,df15])
#print(kf)
#sdf = kf.sort_values(by='name')
#print(sdf)
#sdf.to_csv("/home/raj/Music/SudokuSolvers/read_time/t.csv")

#d = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/t.csv") 
#print(d['algo'].value_counts())


df = pd.concat([df1,df2,df3,df4,df5,df6])
#print(df.loc[df.groupby('name').time.idxmin()])
#print(ldf)
ldf = df.sort_values(by=['name','time']).drop_duplicates(['name'], keep='first')
print(ldf['algo'].value_counts())

#print the number of of solved instances from total 
#n = df['name'].unique()
#b = pd.DataFrame(n, columns=['index', 'words'])
#print(b[0].value_counts())
#print(df.name.str.count("3x3").sum())
#print(df.name.str.count("4x4").sum())
#print(df.name.str.count("5x5").sum())
#print(df.name.str.count("6x6").sum())
#print(df.name.str.count("7x7").sum())
#print(df.name.str.count("8x8").sum())
#print(df.name.str.count("9x9").sum())
