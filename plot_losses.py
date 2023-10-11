import numpy as np
import matplotlib.pyplot as plt

conditional_losses = np.load("conditional_losses.npy")
losses = np.load("losses.npy")

plt.plot(conditional_losses)
plt.plot(losses)
plt.show()