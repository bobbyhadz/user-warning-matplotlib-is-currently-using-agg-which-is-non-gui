# Matplotlib is currently using agg, which is non-GUI backend

import matplotlib

matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi, 150)
y = np.sin(x)

ax = plt.subplot(111)
ax.plot(x, y)

plt.show()