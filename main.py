# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:09:40 2019

@author: Antonio
"""

#%%
import os
import subprocess
import sys

os.chdir(os.path.expanduser("~/Desktop"))
#subprocess.call([sys.executable,'temp.py', 'a', 'b'])
#subprocess.call('temp.py', shell=True)
subprocess.run(['python temp.py'], shell=True)
