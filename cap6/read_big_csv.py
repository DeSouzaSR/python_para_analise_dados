# Read a big csv file using pandas and chuck. 

#%%
# Imports
import pandas as pd

#%%
# Parameter
FILE = '../dados/microdados_censo_escolar_2023/dados/microdados_ed_basica_2023.csv'

#%%
# Read the file with chucksize = 1000 and each loop, store data with CO_UF = 31
df_es = pd.DataFrame()
for chunk in pd.read_csv(FILE, encoding= 'ISO-8859-1', sep=";", chunksize=1000):
    # concatdf_es only data with CO_UF = 32, using concat method
    df_es = pd.concat([df_es, chunk[chunk.CO_UF == 32]])

# %%
