import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import StandardScaler, RobustScaler, QuantileTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

# Seed value
# Apparently you may use different seed values at each stage
#seed_value= 0

# 1. Set `PYTHONHASHSEED` environment variable at a fixed value
#import os
#os.environ['PYTHONHASHSEED']=str(seed_value)

# 2. Set `python` built-in pseudo-random generator at a fixed value
#import random
#random.seed(seed_value)

# 3. Set `numpy` pseudo-random generator at a fixed value
#import numpy as np
#np.random.seed(seed_value)

#load data

train_dataset_path = '/home/users/ubaldi/TESI_PA/data/database_training2.csv'
test_dataset_path = '/home/users/ubaldi/TESI_PA/data/database_nostro_without_nan.csv'

df_train = pd.read_csv(train_dataset_path)
df_test = pd.read_csv(test_dataset_path)

df_train.rename(columns={'Survival.time (months)':'Surv_time_months'}, inplace=True)
df_test.rename(columns={'Survival.time (months)':'Surv_time_months'}, inplace=True)


df_train.rename(columns={'Overall.Stage':'Overall_Stage'}, inplace=True)
df_test.rename(columns={'Overall.Stage':'Overall_Stage'}, inplace=True)

public_data = df_train.drop(['Histology', 'Surv_time_months', 'OS', 'deadstatus.event','Overall_Stage'], axis=1)
PA_data = df_test.drop(['Histology', 'Surv_time_months', 'OS', 'deadstatus.event','Overall_Stage'], axis=1)

public_labels = df_train.Histology
PA_labels = df_test.Histology

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

pca = PCA(copy=True, iterated_power='auto', n_components=10, random_state=None,
    svd_solver='auto', tol=0.0, whiten=False)

GBC = GradientBoostingClassifier(n_estimators=120, max_depth=9)

total_score = []

for sd in np.arange(0,31):

    #Train test split
    X_train, X_test, y_train, y_test = train_test_split(public_data, public_labels, test_size=0.3, stratify=public_labels, random_state=sd)

    #Vettorizzare i label
    train_labels_encoded = encoder.fit_transform(y_train)
    test_labels_encoded = encoder.transform(y_test)

    #scaling
    r_scaler = RobustScaler(copy=True, quantile_range=(25.0, 75.0), with_centering=True, with_scaling=True)
    X_train_scaled = r_scaler.fit_transform(X_train)
    X_test_scaled = r_scaler.transform(X_test)

    #PCA
    X_train_scaled_pca = pca.fit_transform(X_train_scaled)
    X_test_scaled_pca = pca.transform(X_test_scaled)

    #fit model
    GBC.fit(X_train_scaled_pca, y_train)

    #score
    score = GBC.score(X_test_scaled_pca, y_test)

    total_score.append(score)

file_score = open('/home/users/ubaldi/TESI_PA/result_CV/score_test_stability_GBC.txt', 'w')
file_score.write(f'{total_score}')
file_score.close()


total_score_seed_TTS_fissato = []


for i in np.ones((30,), dtype=int):

    #Train test split
    X_train, X_test, y_train, y_test = train_test_split(public_data, public_labels, test_size=0.3, stratify=public_labels, random_state=sd)

    #Vettorizzare i label
    train_labels_encoded = encoder.fit_transform(y_train)
    test_labels_encoded = encoder.transform(y_test)

    #scaling
    r_scaler = RobustScaler(copy=True, quantile_range=(25.0, 75.0), with_centering=True, with_scaling=True)
    X_train_scaled = r_scaler.fit_transform(X_train)
    X_test_scaled = r_scaler.transform(X_test)

    #PCA
    X_train_scaled_pca = pca.fit_transform(X_train_scaled)
    X_test_scaled_pca = pca.transform(X_test_scaled)

    #fit model
    GBC.fit(X_train_scaled_pca, y_train)

    #score
    score = GBC.score(X_test_scaled_pca, y_test)

    total_score_seed_TTS_fissato.append(score)

file_score = open('/home/users/ubaldi/TESI_PA/result_CV/score_test_stability_GBC_seed_TTS_fissato.txt', 'w')
file_score.write(f'{total_score_seed_TTS_fissato}')
file_score.close()
