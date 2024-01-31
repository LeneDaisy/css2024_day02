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

#file = pd.read_json("student_data.json")

print(file)

url = "https://raw.githubusercontent.com/Asabele240701/css4_day02/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"

#df = pd.read_csv(url)


df = pd.read_csv("country_data_index.csv", index_col=0)

df = pd.read_excel("residentdoctors.xlsx")

print(df.info())

df["LOWER_AGE"]=df["AGEDIST"].str.extract('(\d+)-')
# '(\d+)-' --> this means you extract the first number before the hypen 

df["UPPER_AGE"]=df["AGEDIST"].str.extract('-(\d+)')

df["LOWER_AGE"] = df["LOWER_AGE"].astype(int)

print(df.info())

"""
working with dates 

30-01-2024 - UK 
01-30-2024 - US 

"""

df = pd.read_csv("time_series_data.csv", index_col=0)


df['Date']=pd.to_datetime(df['Date'])

#df['Date']=pd.to_datetime(df['Date'], format="%d-%m-%Y")

print(df.info())

df['Year'] = df['Date'].dt.year
#meaning of this line - extracting the year and put it in a new column called 'Year' 

df = pd.read_csv("patient_data_dates.csv", index_col=0)

df.drop(index=26, inplace=True)

df['Date']=pd.to_datetime(df['Date'])

print(df.info())

avg_cal = df["Calories"].mean()

#df["Calories"].fillna(avg_cal, inplace=True)

df.dropna(inplace=True)
#this one drop the entire row, if there is a na NA value in that row

df =df.reset_index(drop=True)

#df.loc[7,'Duration'] = 45

#another way to change 450 to 45 -- next line 
df['Duration']=df['Duration'].replace([450],45)

#print(df)

# pd.set_option('display.max_rows', None)

df = pd.read_csv("iris.csv")

col_names = df.columns.tolist()

print(col_names)

#below two different techniques to do the same thing 

#OPTION 1 
df["sepal_length_sq"] = df['sepal_length']**2

#OPTION 2
df["sepal_length_sq"] = df["sepal_length"].apply(lambda x: x**2)

grouped = df.groupby("class")

mean_square_values = grouped['sepal_length_sq'].mean()

print(mean_square_values)

###################

#df1 = pd.read_csv("person_split1.csv")

#df2 = pd.read_csv("person_split2.csv")

#df = pd.concat([df1,df2], ignore_index=True)

#########

#df1 = pd.read_csv("person_education.csv")

#df2 = pd.read_csv("person_work.csv")

#f_merge_inner = pd.merge(df1, df2, on="id")

print(df)

#remove the "Iris-" part of the names in the column called "class" 
df["class"] = df["class"].str.replace("Iris-", "")

df = df[df['sepal_length'] > 5]

df = df[df["class"]=="virginica"]

df.to_csv("pulsar.csv")

url = "https://raw.githubusercontent.com/alexandrehsd/Predicting-Pulsar-Stars/master/pulsar_stars.csv"

df = pd.read_csv(url)







