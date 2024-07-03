import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import numpy as np


d=pd.read_csv(r"C:\Users\91807\Desktop\dataset\real_estate_texas_500_2024.csv")


#print(d.isnull().sum())


#print(d.info())


#d2=d.fillna(value=0)


#d2=d.fillna(method='bfill')


#d2=d.fillna(method='pad',axis=1)


#d2=d.fillna({'sub_type':'not yet'})


#print(d2.sub_type.head(10))


#d2=d.dropna()


#d2=d.dropna(how="any")


#d2=d.dropna(axis=1)


#d2=d.dropna(subset=['sub_type'])


#d2=d.dropna(thresh=5)


#d2=d.interpolate(method="pad")


#d2=d.replace(to_replace=np.nan,value=0)


print(d2.isnull().sum())
