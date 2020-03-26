#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:33:04 2020

@author: leonardo
"""


import os
import pandas as pd

path = '/home/leonardo/Scrivania/result_CV/regression_OS/Public/large_space_change_expl_TTS_rand_state/*/*.csv'


my_dict = {'MAE_TRAIN_MEAN': [],
           'MAE_TRAIN_STD': [], 
           'MAE_TEST_MEAN': [],
           'MAE_TEST_STD': []}

clf_list = []

import glob
for name in sorted(glob.glob(path)):
    print(name)
    data = pd.read_csv(name) 
    clf = os.path.split(name)[-1]
    clf = clf[12:-18]
    my_dict['MAE_TRAIN_MEAN'].append(data['MAE_train_mean'][0])
    my_dict['MAE_TRAIN_STD'].append(data['MAE_train_std'][0])
    my_dict['MAE_TEST_MEAN'].append(data['MAE_test_mean'][0])
    my_dict['MAE_TEST_STD'].append(data['MAE_test_std'][0])
    clf_list.append(clf)



df = pd.DataFrame(my_dict, index=clf_list)

df.to_csv('/home/leonardo/Scrivania/result_CV/regression_OS/Public/compare_GS_OS_regression.csv')




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

