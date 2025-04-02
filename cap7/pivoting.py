import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(6).reshape((2,3)),
                    index=pd.Index(['Ohio', 'Colorado'], name='state'),
                    columns=pd.Index(['one', 'two', 'three'],
                                     name='number'))

# Organizando os dados por pivoteamento
result = data.stack()

print('\nData')
print(data)
print('\nData Pivoteado')
print(result)