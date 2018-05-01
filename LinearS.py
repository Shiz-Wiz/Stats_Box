items = list()
num = input("Enter how many elements you want: ")
for i in range(int(num)):
    t = input("Element: ")
    items.append(int(t))

x = int(input("Enter item to search: "))

i = flag = 0

while i < len(items):
    if items[i] == x:
        flag = 1
        break

    i = i + 1

if flag == 1:
    print("Item found at position:", i + 1)
else:
    print("Item not found")