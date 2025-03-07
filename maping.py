# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 16:58:14 2025

@author: srsouza
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({'a':range(5), 'b':np.random.random(5)})

df['a'] = [0, 1, 2, 2, 2]
mapping = {0:0, 1:1, 2:10, 3:100, 4:1000}

df['fator'] = df['a'].map(mapping)
