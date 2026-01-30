import numpy as np

m = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])

n = np.array([[[10, 20], [30, 40]],
              [[50, 60], [70, 80]]])

print(np.stack((m, n), axis=0))
print(np.stack((m, n), axis=1))
print(np.stack((m, n), axis=2))
print(np.stack((m, n), axis=3))