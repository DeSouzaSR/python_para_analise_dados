import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

dataset = np.random.randn(1000).cumsum()
xmin = dataset.argmin()
ymin = dataset[xmin]
print(xmin, ymin)


fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)
ax.set_xticks([0, 250, 500, 750, 1000])
#ax.set_xticklabels(['One', 'Two', 'Three', 'Four', 'Five'],
#                        rotation=30, fontsize='small')
ax.set_title('Energy evolution')
ax.set_xlabel('Time [s]')
ax.plot(dataset)
ax.plot(xmin, ymin, 'ro')
ax.annotate('Min', xy=(xmin, ymin), xytext=(xmin + 200, ymin),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()