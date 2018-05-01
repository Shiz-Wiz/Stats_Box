def interpolationSearch(arr, n, x):
    # Find indexs of two corners
    lo = 0
    hi = (n - 1)

    # Since array is sorted, an element present
    # in array must be in range defined by corner
    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        # Probing the position with keeping
        # uniform distribution in mind.
        pos = lo + int(((float(hi - lo) /
                         (arr[hi] - arr[lo])) * (x - arr[lo])))

        # Condition of target found
        if arr[pos] == x:
            return pos

        # If x is larger, x is in upper part
        if arr[pos] < x:
            lo = pos + 1

        # If x is smaller, x is in lower part
        else:
            hi = pos - 1

    return -1


# Driver Code
# Array of items oin which search will be conducted
arr = list()
num = input("Enter how many elements you want: ")
for i in range(int(num)):
    t = input("Element: ")
    arr.append(int(t))

x = int(input("Enter item to search: "))

n = len(arr)
index = interpolationSearch(arr, n, x)

if index != -1:
    print("Element found at position", index+1)
else:
    print("Element not found")
