#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:14:03 2024

@author: lenenortje
"""

import pandas as pd 

file = pd.read_csv("iris.csv")

print(file)

"""
absolute path:
    /Users/lenenortje/Desktop/CHPC coding summer school/week 1/day2/css2024_day2/iris.csv
    
    ---> this is the full path of this file 
    
 relative path:
     iris.csv
     
     ---> location relative to where you currently are 
     
"""

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

print(df)

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)

file = pd.read_csv("Geospatial Data.txt", sep=";")

file = pd.read_excel("residentdoctors.xlsx")

file = pd.read_json("student_data.json")

print(file)

url = "https://raw.githubusercontent.com/Asabele240701/css4_day02/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"

#df = dataframe 

#df = pd.read_csv(url)

df = pd.read_csv("Accelerometer_data.csv", names = ["date_time", "x", "y", "z"])

df = pd.read_json("bin.1.json")







