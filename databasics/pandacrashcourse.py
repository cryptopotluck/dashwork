import pandas as pd
import numpy as np

df = pd.read_csv('salaries.csv')

#call a specifc labe; of the datframe
print(df['Salary'])

#call smallest sallary
print(df['Salary'].min())

#pfing ages higher than 30
print(df[df['Age'] > 30])

#array of unique numbers
print(df['Age'].unique())

#length of unique items list
print(df['Age'].nunique())

#info on dataframe
print(df.info())

#satistical summary of the dataframe
print(df.describe())

#-----------------
#turn a array into a dataframe
mat = np.arange(0,10).reshape(5,2)

df2 = pd.DataFrame(data=mat, columns=['A','B'], index=['Z','X','Y'])