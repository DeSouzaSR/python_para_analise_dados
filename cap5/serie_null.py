#%%
import pandas as pd

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)

# %%
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
# %%
print(obj4)
# %%
# Verificar se é null
print(pd.isnull(obj4))
# %%
# Contando os nulls
print(f'Quantidade de nulls: {pd.isnull(obj4).sum()}')

# %%
# Contando quantidade de não nulos
print(f'Quantidade de não nulos: {pd.notnull(obj4).sum()}')
# %%
