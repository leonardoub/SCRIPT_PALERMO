#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:36:03 2020

@author: leonardo
"""

import os
import pandas as pd

path = '/home/leonardo/Scrivania/result_score/Public/3_histologies/best_params_score/*.csv'
path_NO_NO = '/home/leonardo/Scrivania/result_score/Public/3_histologies/score_NOprep_NOfeatRed/*.csv'
path_YES_NO_MMS = '/home/leonardo/Scrivania/result_score/3_classes_H/Public/score_YESprep_NOfeatRed/*MMS*.csv'
path_YES_NO_STDS = '/home/leonardo/Scrivania/result_score/3_classes_H/Public/score_YESprep_NOfeatRed/*STDS*.csv'
path_YES_NO_RBT = '/home/leonardo/Scrivania/result_score/3_classes_H/Public/score_YESprep_NOfeatRed/*RBT*.csv'


my_dict = {'ACC_TRAIN_MEAN': [],
           'ACC_TRAIN_STD': [], 
           'ACC_TEST_MEAN': [],
           'ACC_TEST_STD': []}

my_dict_NO_NO = {'NO_NO_ACC_TRAIN_MEAN': [],
                 'NO_NO_ACC_TRAIN_STD': [], 
                 'NO_NO_ACC_TEST_MEAN': [],
                 'NO_NO_ACC_TEST_STD': []}

my_dict_YES_NO_MMS = {'YES_MMS_NO_ACC_TRAIN_MEAN': [],
                      'YES_MMS_NO_ACC_TRAIN_STD': [], 
                      'YES_MMS_NO_ACC_TEST_MEAN': [],
                      'YES_MMS_NO_ACC_TEST_STD': []}

my_dict_YES_NO_STDS = {'YES_STDS_NO_ACC_TRAIN_MEAN': [],
                      'YES_STDS_NO_ACC_TRAIN_STD': [], 
                      'YES_STDS_NO_ACC_TEST_MEAN': [],
                      'YES_STDS_NO_ACC_TEST_STD': []}

my_dict_YES_NO_RBT = {'YES_RBT_NO_ACC_TRAIN_MEAN': [],
                      'YES_RBT_NO_ACC_TRAIN_STD': [], 
                      'YES_RBT_NO_ACC_TEST_MEAN': [],
                      'YES_RBT_NO_ACC_TEST_STD': []}

clf_list = []

import glob
for name in glob.glob(path):
    print(name)
    data = pd.read_csv(name) 
    clf = os.path.split(name)[-1]
    clf = clf[12:-4]
    my_dict['ACC_TRAIN_MEAN'].append(data['train_accuracy_MEAN'][0])
    my_dict['ACC_TRAIN_STD'].append(data['train_accuracy_STD'][0])
    my_dict['ACC_TEST_MEAN'].append(data['test_accuracy_MEAN'][0])
    my_dict['ACC_TEST_STD'].append(data['accuracy_test_STD'][0])
    clf_list.append(clf)

df_bp = pd.DataFrame(my_dict, index=clf_list)
        
clf_list_NO_NO = []       
for name in glob.glob(path_NO_NO):
    print(name)
    data = pd.read_csv(name) 
    clf = os.path.split(name)[-1]
    clf = clf[12:-10]
    my_dict_NO_NO['NO_NO_ACC_TRAIN_MEAN'].append(data['train_accuracy_MEAN'][0])
    my_dict_NO_NO['NO_NO_ACC_TRAIN_STD'].append(data['train_accuracy_STD'][0])
    my_dict_NO_NO['NO_NO_ACC_TEST_MEAN'].append(data['test_accuracy_MEAN'][0])
    my_dict_NO_NO['NO_NO_ACC_TEST_STD'].append(data['test_accuracy_STD'][0])
    clf_list_NO_NO.append(clf) 

df_NO_NO = pd.DataFrame(my_dict_NO_NO, index=clf_list_NO_NO)       
               

clf_list_YES_NO_MMS = []       
for name in glob.glob(path_YES_NO_MMS):
    print(name)
    data = pd.read_csv(name) 
    clf = os.path.split(name)[-1]
    clf = clf[12:-7]
    my_dict_YES_NO_MMS['YES_MMS_NO_ACC_TRAIN_MEAN'].append(data['train_accuracy_MEAN'][0])
    my_dict_YES_NO_MMS['YES_MMS_NO_ACC_TRAIN_STD'].append(data['train_accuracy_STD'][0])
    my_dict_YES_NO_MMS['YES_MMS_NO_ACC_TEST_MEAN'].append(data['test_accuracy_MEAN'][0])
    my_dict_YES_NO_MMS['YES_MMS_NO_ACC_TEST_STD'].append(data['test_accuracy_STD'][0])
    clf_list_YES_NO_MMS.append(clf) 

df_YES_NO_MMS = pd.DataFrame(my_dict_YES_NO_MMS, index=clf_list_YES_NO_MMS)       


clf_list_YES_NO_STDS = []       
for name in glob.glob(path_YES_NO_STDS):
    print(name)
    data = pd.read_csv(name) 
    clf = os.path.split(name)[-1]
    clf = clf[12:-7]
    my_dict_YES_NO_STDS['YES_STDS_NO_ACC_TRAIN_MEAN'].append(data['train_accuracy_MEAN'][0])
    my_dict_YES_NO_STDS['YES_STDS_NO_ACC_TRAIN_STD'].append(data['train_accuracy_STD'][0])
    my_dict_YES_NO_STDS['YES_STDS_NO_ACC_TEST_MEAN'].append(data['test_accuracy_MEAN'][0])
    my_dict_YES_NO_STDS['YES_STDS_NO_ACC_TEST_STD'].append(data['test_accuracy_STD'][0])
    clf_list_YES_NO_STDS.append(clf) 

df_YES_NO_STDS = pd.DataFrame(my_dict_YES_NO_STDS, index=clf_list_YES_NO_STDS)       


clf_list_YES_NO_RBT = []       
for name in glob.glob(path_YES_NO_RBT):
    print(name)
    data = pd.read_csv(name) 
    clf = os.path.split(name)[-1]
    clf = clf[12:-7]
    my_dict_YES_NO_RBT['YES_RBT_NO_ACC_TRAIN_MEAN'].append(data['train_accuracy_MEAN'][0])
    my_dict_YES_NO_RBT['YES_RBT_NO_ACC_TRAIN_STD'].append(data['train_accuracy_STD'][0])
    my_dict_YES_NO_RBT['YES_RBT_NO_ACC_TEST_MEAN'].append(data['test_accuracy_MEAN'][0])
    my_dict_YES_NO_RBT['YES_RBT_NO_ACC_TEST_STD'].append(data['test_accuracy_STD'][0])
    clf_list_YES_NO_RBT.append(clf) 

df_YES_NO_RBT = pd.DataFrame(my_dict_YES_NO_RBT, index=clf_list_YES_NO_RBT)      
 


df_tot = pd.concat([df_bp, df_NO_NO, df_YES_NO_MMS, df_YES_NO_STDS, df_YES_NO_RBT], axis=1)

df_tot.to_csv('/home/leonardo/Scrivania/result_score/compare_score_mean_acc_NONO_YESNO_BESTPARAMS_3classes.csv')


















#
#a = os.path.split(name)[-1]
#a = a[12:-4]
#
#b = data['accuracy_train_mean'][0]
#
#
#my_dict = {'ACC_TRAIN_MEAN': [data['accuracy_train_mean'][0]],
#           'ACC_TRAIN_STD': [data['accuracy_train_std'][0]], 
#           'ACC_TEST_MEAN': [data['accuracy_test_mean'][0]],
#           'ACC_Test_std': [data['accuracy_test_std'][0]]}
#
#my_dict['ACC_TRAIN_MEAN'].append(3)
#
#c=pd.DataFrame(my_dict, index=[a])
#c.index.name = 'classifier'



#in caso dovessi concatenare delle colonne con dimensioni diverse conviene fare i
#dataframe di ogni colonna e poi concatenarli usando 
#df_tot = pd.concat([df_1, df_2, df_3, df_4, df_5], axis=1)

