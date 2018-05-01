def binary_search_recursive(a_list, item):
    """Performs recursive binary search of an integer in a given, sorted, list.
    a_list -- sorted list of integers
    item -- integer you are searching for the position of
    """

    first = 0
    last = len(a_list) - 1

    if len(a_list) == 0:
        return '{Item} was not found in the list'.format(Item=item)
    else:
        i = (first + last) // 2
        if item == a_list[i]:
            return 'Item found at position ',i+1
        else:
            if a_list[i] < item:
                return binary_search_recursive(a_list[i+1:], item)
            else:
                return binary_search_recursive(a_list[:i], item)

items = list()
num = input("Enter how many elements you want: ")
for i in range(int(num)):
    t = input("Element: ")
    items.append(int(t))

x = int(input("Enter item to search: "))
print(binary_search_recursive(items, x))