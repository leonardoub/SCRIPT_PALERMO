import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import StandardScaler, RobustScaler, QuantileTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score 
from sklearn.model_selection import cross_validate
from sklearn.metrics import roc_auc_score
from sklearn.metrics import classification_report

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


#vettorizzare i label
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

tot_score = []
tot_macro_ovo = []
tot_weighted_ovo = []
tot_macro_ovr = []
tot_weighted_ovr = []


for i in range(1,31):

    #train test split 
    X_train, X_test, y_train, y_test = train_test_split(public_data, public_labels, test_size=0.3, stratify=public_labels)

    #vettorizzare i label
    train_labels_encoded = encoder.fit_transform(y_train)
    test_labels_encoded = encoder.transform(y_test)


    scaler = RobustScaler()
    pca = PCA(n_components=7)
    svm = SVC(kernel='rbf', probability=True)

    steps = [('scaler', scaler), ('red_dim', pca), ('clf', svm)]    

    pipeline = Pipeline(steps)

    summary = pipeline.named_steps

    pipeline.fit(X_train, train_labels_encoded)

    score = pipeline.score(X_test, test_labels_encoded)
    tot_score.append(score)

    y_scores = pipeline.predict_proba(X_test)

    macro_ovo = roc_auc_score(test_labels_encoded, y_scores, average='macro',  multi_class='ovo')
    weighted_ovo = roc_auc_score(test_labels_encoded, y_scores, average='weighted',  multi_class='ovo')
    macro_ovr = roc_auc_score(test_labels_encoded, y_scores, average='macro',  multi_class='ovr')
    weighted_ovr = roc_auc_score(test_labels_encoded, y_scores, average='weighted',  multi_class='ovr')

    tot_macro_ovo.append(macro_ovo)
    tot_weighted_ovo.append(weighted_ovo)
    tot_macro_ovr.append(macro_ovr)
    tot_weighted_ovr.append(weighted_ovr)

    y_pred = pipeline.predict(X_test)
    
    report = classification_report(test_labels_encoded, y_pred, output_dict=True)
    df_r = pd.DataFrame(report).
    df_r = df_r.transpose()
    df_r.to_csv(f'/home/users/ubaldi/TESI_PA/result_CV/report_svm_rbf/report_{i}')




# pandas can convert a list of lists to a dataframe.
# each list is a row thus after constructing the dataframe
# transpose is applied to get to the user's desired output. 
df = pd.DataFrame([tot_score, tot_macro_ovo, tot_weighted_ovo, tot_macro_ovr, tot_weighted_ovr])
df = df.transpose() 

fieldnames = ['score', 'roc_auc_score_macro_ovo', 'roc_auc_score_weighted_ovo', 
                  'roc_auc_score_macro_ovr', 'roc_auc_score_weighted_ovr']
# write the data to the specified output path: "output"/+file_name
# without adding the index of the dataframe to the output 
# and without adding a header to the output. 
# => these parameters are added to be fit the desired output. 
df.to_csv('/home/users/ubaldi/TESI_PA/result_CV/score_svm_rbf.csv', index=False, header=fieldnames)




