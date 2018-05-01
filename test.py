import numpy as np
from scipy import stats


arr = list()
num = input("Enter how many elements you want: ")
for i in range(int(num)):
    t = input("Element: ")
    arr.append(int(t))
print(np.mean(arr))
print(np.median(arr))
print(stats.mode(arr))