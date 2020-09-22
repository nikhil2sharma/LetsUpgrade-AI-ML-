#Assignment Solution
#Day-17_11_09_2020
#By  : Nikhil Sharma
#Date_Of_Completion : 21-09-2020

import os
os.chdir(r'C:\Official\Work\letsupgrade\Day-13\Assignment')

# Question:
# Prepare a case study for the given Dataset implement the following steps:
# Steps:
# 1. Import different required library
# 2. Check the version of Library
# 3. Go for different observation like Info, description
# 4. Check null Values
# 5. Check duplicate values
# 6. Filter for different condition - come up with insights from the dataset , basic plot , distribution plots
# 7. Use a histogram to plot different column


# 1. Import different required library
import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib as mt
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Check the version of Library
print('Numpy version',np.__version__)
print('Pandas version',pd.__version__)
print('Sklearn version',sk.__version__)
print('matplotlib version',mt.__version__)


# 3. Go for different observation like Info, description
creditcard=pd.read_csv('creditcard.csv')
print(creditcard.head())
print('Info Output>>')
print(creditcard.info())
print('Describe Output')
print(creditcard.describe().transpose())

# 4. Check null Values
print('Check null values')
print(creditcard.isnull().sum())
# print(creditcard.isnull().any())


# 5. Check duplicate values
print('Below code finds whether the row is duplicate and tags TRUE if it is duplicate and tags FALSE if it is not duplicate. And assigns it to the column named “is_duplicate”  of the datafram')
creditcard['is_duplicate'] = creditcard.duplicated()

print('creditcard with highight duplicate value',creditcard.head())


# 6. Filter for different condition - come up with insights from the dataset , basic plot , distribution plots

creditcard_filter=creditcard['V3']>1.77
creditcard[creditcard_filter].head()

# Insights from the dataset

# No missing value (Through isnull function and and count of observations)
# The data is skewed as data mean and 50% huge difference
#Imbalance data (Non Fraudulent Transactions and Fraudulent Transactions)

#Heat map for correlation study
f,ax = plt.subplots(figsize=(20, 20))
sns.heatmap(creditcard.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)






# 7. Use a histogram to plot different column
creditcard.hist(figsize=(20,20))
plt.show()