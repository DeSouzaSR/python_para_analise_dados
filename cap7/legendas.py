import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

N = 50

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(randn(N).cumsum(), 'k', label='One', linewidth=1)
ax.plot(randn(N).cumsum(), 'r^-', label='Two', linewidth=0.4)
ax.plot(randn(N).cumsum(), 'bo-', label='Three', linewidth=0.4)

ax.legend(loc='best')
fig.show()