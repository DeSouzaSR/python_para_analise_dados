# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 16:43:06 2025

@author: srsouza
"""

import pandas as pd

data = pd.DataFrame({'k1': ['one', 'two']*3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4]})

data['v1'] = range(7)

# Permanecer o último
data.drop_duplicates(['k1','k2'],keep='last')