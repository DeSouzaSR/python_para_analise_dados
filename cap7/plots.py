import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

ax1.plot(np.random.randn(50).cumsum(), 'k--')
ax2.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax3.scatter(np.arange(30), np.arange(30) + 3*np.random.randn(30))

plt.show()