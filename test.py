from loadfunctions import *
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import sys

def read_data(path):
    cols  = ['Name', 'Age', 'Hometown', 'Job']
    raw_data = pd.read_excel(path)
    #header_row = find_header(cols, raw_data)
    header_row = find_header_limited(cols, raw_data, 0.10)
    if(header_row != -1):
        data = pd.read_excel(path, header=header_row)
        return data
    else:
        return pd.DataFrame()


print('--------- start testing -------------')

data_1 = pd.DataFrame()
data_2 = pd.DataFrame()
data_3 = pd.DataFrame()
data_4 = pd.DataFrame()

path_1 = "C:/Users/reshs/source/repos/loadpandas/testfiles/Bachelor_1.xlsx"
path_2 = "C:/Users/reshs/source/repos/loadpandas/testfiles/Bachelor_2.xlsx"
path_3 = "C:/Users/reshs/source/repos/loadpandas/testfiles/Bachelor_3.xlsx"
path_4 = "C:/Users/reshs/source/repos/loadpandas/testfiles/Bachelor_4.xlsx"

data_1 = read_data(path_1)

print('-------test data 1 is------------------')
print(data_1.head())

data_2 = read_data(path_2)
print('-------test data 2 is------------------')
print(data_2.head())

data_3 = read_data(path_3)
print('-------test data 3 is------------------')
print(data_3.head())

data_4 = read_data(path_4)
print('-------test data 4 is------------------')
print(data_4.head())
