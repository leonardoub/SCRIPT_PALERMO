#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:40:41 2019

@author: leonardo
"""


data_path = '/home/leonardo/Scrivania/AIM-PA/database_training2.csv'

from sklearn import preprocessing
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import cross_val_score, GridSearchCV, ParameterGrid, train_test_split
from sklearn.svm import SVC



df = pd.read_csv(data_path)
data = df.drop(['Histology', 'Survival.time (months)', 'OS', 'deadstatus.event', 'Overall.Stage'], axis=1)

label = df.loc[:, 'OS']

label = [i.replace('+di4anni', '5') for i in label]
label = [i.replace('_anni', '') for i in label]
label = [i.replace('_anno', '') for i in label]
label = [int(i) for i in label]


X_train, X_test, Y_train, Y_test = train_test_split(data, label)


#STADARDIZATION
scaler = preprocessing.StandardScaler().fit(X_train)
X_train_n = scaler.transform(X_train)  
X_test_n = scaler.transform(X_test)

#PCA
pca = PCA(n_components = 0.95)
reducer = pca.fit(X_train_n)
X1_train_n_reduced = reducer.transform(X_train_n) 
X1_test_n_reduced = reducer.transform(X_test_n)


clf=SVC(C=1, kernel='rbf', gamma=0.1)
clf.fit(X_train_n,Y_train)














