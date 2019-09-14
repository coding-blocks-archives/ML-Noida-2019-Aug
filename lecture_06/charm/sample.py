import numpy as np

try:
    old = np.load("data.npy")
except FileNotFoundError as e:
    old = np.zeros([0, 10001])

print(old[:10, :10])

print(old.dtype)
#
print(old.shape)
#
# y = old[:, 0]
#
# print(y)




