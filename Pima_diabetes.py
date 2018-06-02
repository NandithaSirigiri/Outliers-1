# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 13:15:01 2018

@author: Icheme
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

import seaborn as sns
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
Pima = pd.read_csv('C:\\Users\\Icheme\\Desktop\\ML\\pima-indians-diabetes-data.csv', names = names)

print(Pima)
print(Pima.describe())

Pima.boxplot()
#Pima.hist()
Pima.groupby('class').hist()
Pima.groupby('class').plas.hist(alpha=0.4)
