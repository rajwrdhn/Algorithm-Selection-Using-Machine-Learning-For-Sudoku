import pandas as pd 
import numpy as np

data = pd.read_csv("featurescompleteheader3_9.csv")
# sorting by first name
data.sort_values('name_puzzle',inplace = True)
 
# dropping ALL duplicate values
data.drop_duplicates(keep = False, inplace = True)
data.drop_duplicates()
#print(data.iloc[: , 1:])



data1 = pd.read_csv("featurescompleteheader4_9.csv")
# sorting by first name
data1.sort_values('name_puzzle',inplace = True)
 
# dropping ALL duplicate values
data1.drop_duplicates(keep = False, inplace = True)
#print(data1.iloc[: , 1:])


#make regression data foreach solver
#order 3 to 9
chtime = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/chuffed/chtime.csv")
chtime = chtime.iloc[:,1:8]
chtime = chtime.drop(columns= ['time', 'pathschuf'])
chtime = chtime.rename(columns = {'name': 'name_puzzle'})


regressiondatachuf = pd.merge(data,chtime)
#regressiondatachuf = regressiondatachuf.drop(columns=['Unnamed: 0'])

#regressiondatachuf.to_csv("regression_chuf_3_9.csv")


#dropping comtime for others
#regressiondatachuf = regressiondatachuf.drop(columns=['comtime'])
print(regressiondatachuf)

cptime = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/cplex/cptime.csv")
cptime = cptime.drop(columns=['Unnamed: 0','time', 'pathscplex', 'flatintvarscplex',  'flatintconstraintscplex',  'flattimecplex'])
cptime = cptime.rename(columns = {'name': 'name_puzzle'})
#print(cptime)
regressiondatacplex = pd.merge(regressiondatachuf,cptime)
regressiondatacplex = regressiondatacplex.drop(columns=['Unnamed: 0'])
#print(regressiondatacplex)

#regressiondatacplex.to_csv("regression_cplex_3_9.csv")

gutime = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/gurobi/gutime.csv")
#cptime = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/cplex/cptime.csv")
gutime = gutime.drop(columns=['Unnamed: 0','time', 'pathsgurobi', 'flatintvarsgurobi',  'flatintconstraintsgurobi',  'flattimegurobi'])
gutime = gutime.rename(columns = {'name': 'name_puzzle'})
#print(cptime)
regressiondatagurobi = pd.merge(regressiondatachuf,gutime)
regressiondatagurobi = regressiondatagurobi.drop(columns=['Unnamed: 0'])
#print(regressiondatagurobi)

#regressiondatagurobi.to_csv("regression_gurobi_3_9.csv")


hytime = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/hybrid/hyilstime.csv")
hytime = hytime.rename(columns = {'name': 'name_puzzle','time':'comtime'})
regressiondatahyils = pd.merge(regressiondatachuf,hytime)
regressiondatahyils = regressiondatahyils.drop(columns=['Unnamed: 0'])
#print(regressiondatahyils)
#regressiondatahyils.to_csv("regression_hyils_3_9.csv")

ortime = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/or/ortime.csv")
ortime = ortime.rename(columns = {'name': 'name_puzzle','time':'comtime'})
regressiondataortool = pd.merge(regressiondatachuf,ortime)
regressiondataortool = regressiondataortool.drop(columns=['Unnamed: 0'])
#print(regressiondataortool)
#regressiondataortool.to_csv("regression_ortool_3_9.csv")

satime = pd.read_csv("/home/raj/Music/SudokuSolvers/read_time/sa/satime.csv")

satime = satime.rename(columns = {'name': 'name_puzzle','time':'comtime'})
regressiondatasa = pd.merge(regressiondatachuf,satime)
regressiondatasa = regressiondatasa.drop(columns=['Unnamed: 0'])
#print(regressiondatasa)
#regressiondatasa.to_csv("regression_sa_3_9.csv")


regressiondatachuf1 = pd.read_csv("regression_chuf_3_9.csv")
#order 4to 9
index_names1 = regressiondatachuf1[ regressiondatachuf1['order_puzzle'] == '3.0' ].index
#print(index_names)
regressiondatachuf1.drop(index_names1, inplace = True)
#print(regressiondatachuf)
regressiondatachuf1 = regressiondatachuf1.drop(columns=['Unnamed: 0'])
regressiondatachuf1['algo'] = 'chuf'
regressiondatachuf1.to_csv("regression_chuf_4_9.csv")



index_names2 = regressiondatacplex[ regressiondatacplex['order_puzzle'] == '3.0' ].index
#print(index_names)
regressiondatacplex['algo'] = 'cplex'
regressiondatacplex.drop(index_names2, inplace = True)
#print(regressiondatacplex)
#regressiondatacplex.to_csv("regression_cplex_4_9.csv")


index_names3 = regressiondatagurobi[ regressiondatagurobi['order_puzzle'] == '3.0' ].index
#print(index_names)
regressiondatagurobi['algo'] = 'gurobi'
regressiondatagurobi.drop(index_names3, inplace = True)
#print(regressiondatagurobi)
#regressiondatagurobi.to_csv("regression_gurobi_4_9.csv")


index_names4 = regressiondatahyils[ regressiondatahyils['order_puzzle'] == '3.0' ].index
#print(index_names)
regressiondatahyils['algo'] = 'hyils'
regressiondatahyils.drop(index_names4, inplace = True)
print(regressiondatahyils)
#regressiondatahyils.to_csv("regression_hyils_4_9.csv")


index_names5 = regressiondataortool[ regressiondataortool['order_puzzle'] == '3.0' ].index
#print(index_names)
regressiondataortool['algo'] = 'ortl'
regressiondataortool.drop(index_names5, inplace = True)
print(regressiondataortool)
#regressiondataortool.to_csv("regression_or_4_9.csv")

index_names = regressiondatasa[ regressiondatasa['order_puzzle'] == '3.0' ].index
#print(index_names)
regressiondatasa['algo'] = 'sima'
regressiondatasa.drop(index_names, inplace = True)
print(regressiondatasa)
#regressiondatasa.to_csv("regression_sima_4_9.csv")
#make classification data 

#order 3 to 9

#order 4 to 9
dataclassification1 = pd.concat([regressiondatachuf,regressiondatacplex,regressiondatagurobi
                                , regressiondatahyils,regressiondataortool,regressiondatasa])

#dataclassification1.to_csv("classification_4_9.csv")
print(dataclassification1)