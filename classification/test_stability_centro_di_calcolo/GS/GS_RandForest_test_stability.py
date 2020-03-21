
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier


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

#Train test split

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(public_data, public_labels, test_size=0.3, stratify=public_labels, random_state=1)

#Vettorizzare i label

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
train_labels_encoded = encoder.fit_transform(y_train)
test_labels_encoded = encoder.transform(y_test)


#Scalers

from sklearn.preprocessing import StandardScaler, RobustScaler
scalers_to_test = [StandardScaler(), RobustScaler()]

# Designate distributions to sample hyperparameters from 

n_features_to_test = np.arange(1, 11)

n_tree = np.arange(10, 120, 5)


#RandomForestClassifier

for i in range(1,11):

    steps = [('scaler', StandardScaler()), ('red_dim', PCA()), ('clf', RandomForestClassifier(random_state=i*1000))]

    pipeline = Pipeline(steps)

    n_features_to_test = np.arange(1, 11)

    parameteres = [{'scaler':scalers_to_test, 'red_dim':[PCA()], 'red_dim__n_components':list(n_features_to_test),
                    'clf__n_estimators':list(n_tree)}]

    from sklearn.model_selection import GridSearchCV 

    grid = GridSearchCV(pipeline, param_grid=parameteres, cv=3, n_jobs=-1, verbose=1)

    grid.fit(X_train, y_train)

    score = grid.score(X_test, y_test)
    best_p = grid.best_params_


    file_best_params = open(f'/home/users/ubaldi/TESI_PA/result_CV/GS_RandForest_stability/best_params_rs{i*1000}_acc_{score}.txt', 'w')
    file_best_params.write(f'{best_p}')
    file_best_params.close()



