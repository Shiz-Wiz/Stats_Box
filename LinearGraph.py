xc = list()
yc = list()
num = input("Enter how many elements you want:")
print ('Enter the Co-Ordinates : ')
for i in range(int(num)):
    x = input("X Co-Ordinate :")
    y = input("Y Co-Ordinate :")
    xc.append(int(x))
    yc.append(int(y))
with open("example.txt", "w") as f:
    for i in range(int(num)):
        #print ('XC ',xc[i])
        #print ('YC ',yc[i])
        f.write(str(xc[i]) + ',' + str(yc[i]) + '\n')
import gPlotting
gPlotting
#print ('XC ',xc[0])
#print ('YC ',yc[1])