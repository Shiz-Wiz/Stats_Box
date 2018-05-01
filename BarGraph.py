import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

label = list()
y = list()
num = input("Enter Number of Towers")
for i in range(int(num)):
    l = input('Enter Label For tower ')
    yt = input("Enter height of Tower")
    y.append(yt)
    label.append(l)

index = np.arange(len(label))
plt.bar(index, y, align='center', alpha=0.5)
plt.xticks(index, label)
plt.ylabel('Height')
plt.title('Relative bar Graph')

plt.show()
