#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:02:56 2019

@author: leonardo
"""

data_path = '/home/leonardo/Scrivania/AIM-PA/database_training2.csv'

from sklearn import preprocessing
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


df = pd.read_csv(data_path)
data = df.drop(['Histology', 'Survival.time (months)', 'OS', 'deadstatus.event', 'Overall.Stage'], axis=1)

label = df.loc[:, 'OS']

label = [i.replace('+di4anni', '5') for i in label]
label = [i.replace('_anni', '') for i in label]
label = [i.replace('_anno', '') for i in label]


#STADARDIZATION
scaler = preprocessing.StandardScaler().fit(data)
data_n = scaler.transform(data)  

#PCA
pca = PCA(n_components=0.95)
reducer = pca.fit(data_n)
data_n_reduced=reducer.transform(data_n)  


km = KMeans()









