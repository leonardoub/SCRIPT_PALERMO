#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:40:41 2019

@author: leonardo
"""


data_path = '/home/leonardo/Scrivania/AIM-PA/database_training2.csv'

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, roc_auc_score, confusion_matrix
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
X_train_n_reduced = reducer.transform(X_train_n) 
X_test_n_reduced = reducer.transform(X_test_n)


clf=SVC(C=1, kernel='rbf', gamma=0.1)
clf.fit(X_train_n_reduced,Y_train)
Y_test_pred=clf.predict(X_test_n_reduced)
Y_train_pred=clf.predict(X_train_n_reduced)


##VALUTAZIONE

#TRAIN SET

#matrice di confusione

confmat = confusion_matrix(y_true=Y_train, y_pred=Y_train_pred)

fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
            ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')
plt.xlabel('predicted label')
plt.ylabel('true label')
plt.show()


acc_score=accuracy_score(Y_train,Y_train_pred)
print(f'Accuratezza sul train set: {acc_score}')

prec_score=precision_score(Y_train,Y_train_pred, average='weighted')
print('Precisione sul train set: %.3f' % prec_score)

rec_score=recall_score(Y_train,Y_train_pred, average='weighted')
print('Recall sul train set: %.3f' % rec_score)

F1_score=f1_score(Y_train,Y_train_pred, average='weighted')
print('F1 score sul train set: %.3f' % F1_score)

#TEST SET

#matrice di confusione

confmat = confusion_matrix(y_true=Y_test, y_pred=Y_test_pred)

fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
            ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')
plt.xlabel('predicted label')
plt.ylabel('true label')
plt.show()


print('Accuratezza sul test set: %.3f' % clf.score(X_test_n_reduced, Y_test))

prec_score=precision_score(Y_test, Y_test_pred, average='weighted')
print('Precisione sul test set: %.3f' % prec_score)

rec_score=recall_score(Y_test, Y_test_pred, average='weighted')
print('Recall sul test set: %.3f' % rec_score)

F1_score=f1_score(Y_test, Y_test_pred, average='weighted')
print('F1 score sul test set: %.3f' % F1_score)
























