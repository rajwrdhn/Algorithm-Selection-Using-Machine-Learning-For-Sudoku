import pandas
import numpy
import re
import os
import visualize
import seaborn as sns
import xlwt

def join_datasets():
    """Join the dataset for the various algorithms."""
    data_sa = pandas.read_csv('clean_data/sa.csv')
    data_hyls = pandas.read_csv('clean_data/hy_l')
    data_chuf = pandas.read_csv('clean_data/chuf')
    data_cplex = pandas.read_csv('clean_data/cplex')
    data_or = pandas.read_csv('clean_data/or')
    data_gurobi = pandas.read_csv('clean_data/gurobi')

    #merge 
    #concat the dataset time
    

    df_1 = data_sa.append(data_or)
    df_2 = df_1.append(data_hyls)
    df_3 = df_2.append(data_gurobi)
    df_4 = df_3.append(data_cplex)
    df_5 = df_4.append(data_chuf)
    #df_5 has all the times of the algorithms along with names
    remove_similar(df_5)

def remove_similar(df):
    """Remove the similar data with more time limits and keep the better time."""
    df.sort_values(["name", "algo", "time"], inplace = True)
    df.drop_duplicates(subset =["name","algo"],keep="first",inplace=True)
    #df.sort_values(['time'], inplace = True)
    #df.to_csv('out2.csv', index=False)
    #df.to_excel('out2.xls', index=False)
    print(df)
    x =visualize.scatter_plot(df)
    #x.multiple_line_chart()
    x.bar_plot()
    #x.heat_map_plot()

def collect_same(df):
    """collect the data with same names for comparison"""
    #df_sa = 
    
def collect_merged(df):
    """collect the merged data with the same name"""

def collect_different(df):
    """collect the data with different names for comparison"""

def combine_all():
    """combine the dataset of time performance of each algorithm."""
    return 0

def identify_missing_data_time():
    """Here we will identify which puzzles time we do not have and try them again at a later stage."""
    return 0

def three_Five():
    return 0

def easy_df():
    return 0

def hard_df():
    return 0 

def medium_df():
    return 0 

def main():
    join_datasets()

if __name__ == "__main__":
    main()