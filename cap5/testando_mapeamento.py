#%%
import pandas as pd
import numpy as np

#%%
# Dataframe 4 x 4 com dados randômicos entre 0 e 1
frame = pd.DataFrame(np.random.rand(4, 4), columns=list('abcd'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# %%
# Usando applymap para transformar cada elemento em ponto flutuante com duas casas decimais
bla = lambda x: f'{x:.2f}'
frame.applymap(bla)
# %%

# %%
