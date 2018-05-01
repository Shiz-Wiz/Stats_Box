import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = list()
sizes = list()
explode = list()
num = input("Enter Number of Sectors")
for i in range(int(num)):
    x = input("Labels :")
    y = input("% Share :")
    e = input ("Explode or Not (1/0)")
    labels.append(str(x))
    sizes.append(int(y))
    explode.append(int(e)*0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()