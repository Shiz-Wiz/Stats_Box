def insertionSort(arr):

# Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Driver code to test above
arr = list()
num = input("Enter how many elements you want: ")
for i in range(int(num)):
    t = input("Element: ")
    arr.append(int(t))

insertionSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])