# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:51:56 2019

@author: Antonio
"""
#%%
print('executed')

print("The arguments are: " , str(sys.argv))

import pandas as pd

pd.DataFrame(sys.argv).to_csv('test.csv')
pd.DataFrame([1,2,3,4,1000,3223]).to_csv('test.csv')

#return 'sas'