#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:36:23 2020

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

path = '/home/leonardo/Scrivania/result_CV/4_classes_OS/Public/large_space_change_expl_TTS_rand_state/*/*.csv'


my_dict = {'ACC_TRAIN_MEAN': [],
           'ACC_TRAIN_STD': [], 
           'ACC_TEST_MEAN': [],
           'ACC_TEST_STD': []}

clf_list = []

import glob
for name in sorted(glob.glob(path)):
    print(name)
    data = pd.read_csv(name) 
    clf = os.path.split(name)[-1]
    clf = clf[12:-17]
    my_dict['ACC_TRAIN_MEAN'].append(data['accuracy_train_mean'][0])
    my_dict['ACC_TRAIN_STD'].append(data['accuracy_train_std'][0])
    my_dict['ACC_TEST_MEAN'].append(data['accuracy_test_mean'][0])
    my_dict['ACC_TEST_STD'].append(data['accuracy_test_std'][0])
    clf_list.append(clf)



df = pd.DataFrame(my_dict, index=clf_list)

df.to_csv('/home/leonardo/Scrivania/result_CV/compare_GS_OS_4_classes.csv')




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

