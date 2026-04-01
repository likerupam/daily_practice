import numpy as np 

arr = np.array([1, 99, 10, 100, 2, 22, 15, 200, 25, 30])

print(arr[(arr > 10) & (arr < 30)])
