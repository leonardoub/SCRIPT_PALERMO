#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:02:56 2019

@author: leonardo
"""

data_path = '/home/leonardo/Documenti/Uni/Tesi/AIM-PA/database_training2.csv'

import pandas as pd

df = pd.read_csv(data_path)
data = df.drop(['Histology', 'Survival.time (months)', 'OS', 'deadstatus.event', 'Overall.Stage'], axis=1)

label = df.loc[:, 'OS']