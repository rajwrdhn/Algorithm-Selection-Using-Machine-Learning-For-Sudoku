#!usr/var/python
import csv
import pandas as pd 
import os

def create_dataset_feature():
    fields= []#'col1', 'col2', 'col3', 'col4', 'col5',
            #'col6', 'col7', 'col8','col9', 'col10']
    #for i in range(20):
    #fields.append('S_F_'+ str(i))
    #print(fields)
    
    df = pd.DataFrame(fields)
    df.to_csv('features.csv')
    
create_dataset_feature()
