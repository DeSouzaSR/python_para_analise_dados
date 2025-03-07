# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 15:52:34 2025

@author: srsouza
"""

# Explora preenchimento de valores ausentes

import pandas as pd
import numpy as np

# Dataframe
df = pd.DataFrame(np.random.randn(6,3))

# Preenchendo com valores NAs
df.iloc[2:,1] = np.nan
df.iloc[4:,2] = np.nan

# Transferindo o valor para outro dataframe
data = df.copy()
data2 = df.copy()

# Renomeando colunas
data.rename({0:'pri', 1:'seg', 2:'ter'}, axis=1, inplace=True)

# Preenchendo dados ausentes com média
data['seg'] = data['seg'].fillna(data['seg'].mean())

# Preenchendo tudo. Neste caso, ele preenche a coluna automaticamente.
data2 = data2.fillna(data2.mean())