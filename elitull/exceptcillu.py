import numpy as np

x = np.array([0., 1., 1.5, 3.5, 4., 6.], dtype=float)
gradient = np.gradient(x)

print(gradient)
