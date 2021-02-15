import numpy as np

array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [123, 2, 3],
                  3, 3, 3])
# array = np.ones((3, 4), dtype=int)
# array = np.zeros_like((3, 4, 3, 5), dtype=int)
array = np.full((3, 4), 4) # make an array of 4s
# array.diagonal()
print(array)
