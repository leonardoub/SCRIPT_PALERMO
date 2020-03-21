#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:36:03 2020

@author: leonardo
"""

import os
import pandas as pd

path = '/home/leonardo/Scrivania/result_CV/3_classes_H/Public/large_space_change_expl_TTS_rand_state/*/*.csv'
path_anova = '/home/leonardo/Scrivania/result_CV/3_classes_H/Public/only_ANOVA_f_red_change_expl_TTS_rand_state/*/*.csv'
path_kw = '/home/leonardo/Scrivania/result_CV/3_classes_H/Public/only_KW_f_red_change_expl_TTS_rand_state/*/*.csv'


my_dict = {'ACC_TRAIN_MEAN': [],
           'ACC_TRAIN_STD': [], 
           'ACC_TEST_MEAN': [],
           'ACC_TEST_STD': [],
           'ANOVA_ACC_TRAIN_MEAN': [],
           'ANOVA_ACC_TRAIN_STD': [], 
           'ANOVA_ACC_TEST_MEAN': [],
           'ANOVA_ACC_TEST_STD': [],
           'KW_ACC_TRAIN_MEAN': [],
           'KW_ACC_TRAIN_STD': [], 
           'KW_ACC_TEST_MEAN': [],
           'KW_ACC_TEST_STD': []}

clf_list = []

import glob
for name in sorted(glob.glob(path)):
    print(name)
    data = pd.read_csv(name) 
    clf = os.path.split(name)[-1]
    clf = clf[12:-4]
    my_dict['ACC_TRAIN_MEAN'].append(data['accuracy_train_mean'][0])
    my_dict['ACC_TRAIN_STD'].append(data['accuracy_train_std'][0])
    my_dict['ACC_TEST_MEAN'].append(data['accuracy_test_mean'][0])
    my_dict['ACC_TEST_STD'].append(data['accuracy_test_std'][0])
    clf_list.append(clf)

        
clf_list_ANOVA = []       
for name in sorted(glob.glob(path_anova)):
    print(name)
    data = pd.read_csv(name) 
    clf = os.path.split(name)[-1]
    clf = clf[12:-10]
    my_dict['ANOVA_ACC_TRAIN_MEAN'].append(data['accuracy_train_mean'][0])
    my_dict['ANOVA_ACC_TRAIN_STD'].append(data['accuracy_train_std'][0])
    my_dict['ANOVA_ACC_TEST_MEAN'].append(data['accuracy_test_mean'][0])
    my_dict['ANOVA_ACC_TEST_STD'].append(data['accuracy_test_std'][0])
    clf_list_ANOVA.append(clf)        
               

clf_list_KW = []       
for name in sorted(glob.glob(path_kw)):
    print(name)
    data = pd.read_csv(name) 
    clf = os.path.split(name)[-1]
    clf = clf[12:-7]
    my_dict['KW_ACC_TRAIN_MEAN'].append(data['accuracy_train_mean'][0])
    my_dict['KW_ACC_TRAIN_STD'].append(data['accuracy_train_std'][0])
    my_dict['KW_ACC_TEST_MEAN'].append(data['accuracy_test_mean'][0])
    my_dict['KW_ACC_TEST_STD'].append(data['accuracy_test_std'][0])
    clf_list_KW.append(clf) 


if clf_list == clf_list_ANOVA == clf_list_KW:

    df = pd.DataFrame(my_dict, index=clf_list)

    df.to_csv('/home/leonardo/Scrivania/result_CV/compare_GS_mean_acc_ANOVA_KW_3_classes.csv')




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

