import pandas as pd
import math

df = pd.read_csv("/home/raj/Music/MachineLearning/regression/data/original/flatlpdata.csv")
print(df['name_puzzle'])
print(df["flattimecplex"].mean())
print(df["flattimegurobi"].mean())

print(df['flatintvarscplex'].equals(df['flatintvarsgurobi']))
print(df['flatintconstraintscplex'].equals(df['flatintconstraintsgurobi']))