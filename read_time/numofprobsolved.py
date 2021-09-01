
import pandas as pd 


df1 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/sa/satime.csv", )
df1 = df1.fillna(0)
df1['algo'] = 'sima'
df1['comtime'] = df1['time']

df2 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/or/ortime.csv")
df2 = df2.fillna(0)
df2['algo'] = 'ortl'
df2['comtime'] = df2['time']

df3 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/chuffed/chuftime.csv")
df3 = df3.fillna(0)
df3['algo'] = 'chuf'

df4 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/cplex/cplextime.csv")
df4 = df4.fillna(0)
df4['algo'] = 'cplex'

df5 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/gurobi/gurobitime.csv")
df5 = df5.fillna(0)
df5['algo'] = 'gurobi'

df6 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/hybrid/hyilstime.csv")
df6 = df6.fillna(0)
df6['algo'] = 'hyils'
df6['comtime'] = df6['time']

df7 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/chuffed/chtime.csv")
df7 = df7.fillna(0)
df8 = df3.merge(df7)
df9 = df8[['name','comtime','algo']]

df10 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/cplex/cptime.csv")
df10 = df10.fillna(0)
df11 = df4.merge(df10)
df12 = df11[['name','comtime','algo']]

df13 = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/gurobi/gutime.csv")
df13 = df13.fillna(0)
df14 = df5.merge(df13)
df15 = df14[['name','comtime','algo']]

kf = pd.concat([df1,df2,df6,df9,df12,df15])
print(kf['algo'].value_counts())
kf['al'] = kf['algo']
#print(kf.iloc[:3])
#kf = kf['time'].isnull()
#kf = kf.iloc[:3]
kf = kf.set_index('al')
kf = kf.drop(['cplex', 'gurobi', 'sima'])
#print(kf)
sdf = kf.sort_values(by=['name','comtime']).drop_duplicates(['name'], keep='first')
#print(sdf)
#sdf['nam'] = sdf['name']
#sdf = sdf.set_index('nam')
sdf = sdf[sdf.columns.drop(list(sdf.filter(regex='benchmarks3x3')))]
#print(sdf)
print(sdf['algo'].value_counts())
#sdf.to_csv("/home/raj/Music/SudokuSolvers/read_time/t.csv")

#d = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/t.csv") 
#print(d['algo'].value_counts())

df = pd.concat([df1,df2,df3,df4,df5,df6])
#d = df.merge(kf, how='left', indicator=True)
#d[d['_merge'] == 'left_only'][['name']]
#df = df.drop()
#print(df.loc[df.groupby('name').time.idxmin()])
#print(df)
ldf = df.sort_values(by=['name','time']).drop_duplicates(['name'], keep='first')
print(ldf['algo'].value_counts())
#j = df.merge(kf, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only']

#Fill all NaN values with 0
df = df.fillna(0)
#print(df)

#print the number of of solved instances from total 
#n = df['name'].unique()
#b = pd.DataFrame(n, columns=['index', 'words'])
#print(b[0].value_counts())

#Number of "name" column in the df with the string value "3x3"
#print(df.name.str.count("3x3").sum())
#print(df.name.str.count("4x4").sum())
#print(df.name.str.count("5x5").sum())
#print(df.name.str.count("6x6").sum())
#print(df.name.str.count("7x7").sum())
#print(df.name.str.count("8x8").sum())
#print(df.name.str.count("9x9").sum())
