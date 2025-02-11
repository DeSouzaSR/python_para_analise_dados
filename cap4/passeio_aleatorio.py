#%%
# Random Walk
#Implementação do passeio aleatório, usanddo random do numpy.

#%%
import numpy as np
import matplotlib.pyplot as plt
import random

#%%
# Passeio aleatório com 1000 passos, em python
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if  random.randint(0, 1) else -1
    position += step
    walk.append(position)

#%%
plt.plot(walk)
plt.show()


# %%
# Passeio aleatório usando numpy
nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()

#%%
# Plotando passeio aleatório com numpy
plt.plot(walk)
plt.show()

# %%
# Simulando vários passeios aleatórios em um único gráfico
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)

#%%
# Plotando vários passeios aleatórios
plt.plot(walks.T)
plt.show()

# %%
