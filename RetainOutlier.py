# -*- coding: utf-8 -*-
"""
Created on Wed May 16 23:55:38 2018

@author: Icheme
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


from scipy.stats import norm
Data = pd.read_csv('C:\\Users\\Icheme\\Desktop\\ML\\Saven\\AEO2017_output_10000-records.csv')
print(Data)
#print(Data.info())
#print(Data.columns)


c1 = Data[['data_value']]
print(c1)
d1 = Data.sort_values(['data_value'], ascending = False)
print(d1)
Data.boxplot(column=['data_value'])

print(d1.describe())
mu=163.017551 
sigma = 740.403676
column = pd.iloc[Data[data_value]]
print(column)
z=abs(mu-pd.d1)/sigma
print(z)
plt.figure(1)

#plt.title('Histogram')

#dist=normal(mu,sigma)







