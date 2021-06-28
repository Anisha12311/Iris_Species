# Data preprocessing

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

iris = pd.read_csv('Iris.csv')
print(iris.head())

# ---------------------***********************----------------------------

# unique 

print(iris['Species'].unique())

# describe

# ---------------------***********************----------------------------

print(iris.describe(include = 'all'))

# information about dataset

# ---------------------***********************----------------------------

print(iris.info())

# ---------------------***********************----------------------------

# drop the unneeded columns 

print(iris.drop(columns='Id',inplace  = True))

# ---------------------***********************----------------------------

# Check missing values

print(iris.isnull().sum())

import missingno as msno
dt = msno.bar(iris,figsize = (8,6),color = 'pink')
plt.show()
print(dt)




