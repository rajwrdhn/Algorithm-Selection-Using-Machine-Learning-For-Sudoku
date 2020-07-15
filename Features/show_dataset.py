import pandas as pd 

def show():
    df = pd.read_csv('features.csv')
    print(df.head())

show()