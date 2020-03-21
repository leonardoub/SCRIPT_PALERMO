#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:42:00 2020

@author: leonardo
"""

import pandas as pd

path = '/home/leonardo/Scrivania/result_CV/*/*/*/*/*.csv'

import glob
for name in glob.glob(path):
    #print(name)
    data = pd.read_csv(name) 

    acc_train_mean = data['accuracy_train'].mean()
    acc_test_mean = data['accuracy_test'].mean()
    
    acc_train_std = data['accuracy_train'].std()
    acc_test_std = data['accuracy_test'].std()


    df_train_acc_mean = pd.DataFrame([{'accuracy_train_mean':acc_train_mean}])
    df_train_acc_std = pd.DataFrame([{'accuracy_train_std':acc_train_std}])

    
    df_test_acc_mean = pd.DataFrame([{'accuracy_test_mean':acc_test_mean}])
    df_test_acc_std = pd.DataFrame([{'accuracy_test_std':acc_test_std}])


    df = pd.concat([data, df_train_acc_mean, df_train_acc_std, df_test_acc_mean, df_test_acc_std], axis=1)

    df.to_csv(name)


#data = pd.read_csv(name) 

#acc_train_mean = data['accuracy_train'].mean()

#data['accuracy_train'] = acc_train_mean




