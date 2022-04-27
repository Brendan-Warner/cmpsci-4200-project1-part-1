# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
from datetime import datetime
from sklearn import preprocessing
import matplotlib.pyplot as plt

files.upload()

df = pd.read_csv('./clean_data.csv')

#df.dtypes
df


#pf = df.sample(n=500)

#plot = sns.pairplot(pf, hue= 'Target')
#plot = plot.map_upper(plt.scatter)
#plot = plot.map_lower(sns.kdeplot)

#sns.set(rc={'figure.figsize':(13,9)})

#plot = sns.barplot(x='Family_status', y ='Total_income', data = df, hue='Target')
#plot = sns.barplot(data = df, x='Education_type', y = 'Total_income', hue = "Target")
#plot = sns.barplot(data=df, x = 'Family_status', y= 'Target')
#plot = sns.scatt(data = df, x = 'Account_length', y = 'Total_income', hue = 'Target')
#plot = sns.barplot(data=df, x = 'Family_status', y= 'Total_income')
#plot = sns.barplot(data = df, x='Education_type', y = "Target")
#plot = sns.barplot(data = df, x ='Own_property', y =df.groupby('Own_property')['Total_income'].transform('mean'))
