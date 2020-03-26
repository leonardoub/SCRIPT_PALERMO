#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:34:58 2020

@author: leonardo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:36:03 2020

@author: leonardo
"""

import os
import pandas as pd

path_3_classes = '/home/leonardo/Scrivania/result_CV/3_classes_H/Public/large_space_change_expl_TTS_rand_state/*/*.csv'
path_2_classes = '/home/leonardo/Scrivania/result_CV/2_classes_H/Public/large_space_change_expl_TTS_rand_state/*/*.csv'


my_dict = {'3_classes_ACC_TRAIN_MEAN': [],
           '3_classes_ACC_TRAIN_STD': [], 
           '3_classes_ACC_TEST_MEAN': [],
           '3_classes_ACC_TEST_STD': [],
           '2_classes_ACC_TRAIN_MEAN': [],
           '2_classes_ACC_TRAIN_STD': [], 
           '2_classes_ACC_TEST_MEAN': [],
           '2_classes_ACC_TEST_STD': []}

clf_list_3 = []
import glob
for name in glob.glob(path_3_classes):
    print(name)
    data = pd.read_csv(name) 
    clf = os.path.split(name)[-1]
    clf = clf[12:-4]
    my_dict['3_classes_ACC_TRAIN_MEAN'].append(data['accuracy_train_mean'][0])
    my_dict['3_classes_ACC_TRAIN_STD'].append(data['accuracy_train_std'][0])
    my_dict['3_classes_ACC_TEST_MEAN'].append(data['accuracy_test_mean'][0])
    my_dict['3_classes_ACC_TEST_STD'].append(data['accuracy_test_std'][0])
    clf_list_3.append(clf)

        
clf_list_2 = []       
for name in glob.glob(path_2_classes):
    print(name)
    data = pd.read_csv(name) 
    clf = os.path.split(name)[-1]
    clf = clf[12:-14]
    my_dict['2_classes_ACC_TRAIN_MEAN'].append(data['accuracy_train_mean'][0])
    my_dict['2_classes_ACC_TRAIN_STD'].append(data['accuracy_train_std'][0])
    my_dict['2_classes_ACC_TEST_MEAN'].append(data['accuracy_test_mean'][0])
    my_dict['2_classes_ACC_TEST_STD'].append(data['accuracy_test_std'][0])
    clf_list_2.append(clf)        
               


df = pd.DataFrame(my_dict, index=clf_list_3)

df.to_csv('/home/leonardo/Scrivania/result_CV/compare_GS_mean_acc_3_2_classes.csv')





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

