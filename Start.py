print ('Choose from options below')
print ('1. Graphing')
print ('2. Sorting')
print ('3. Searching')
print ('4. Statistical Analysis')
ch = input('Enter your Choice: ')
if (ch =='1'):
    print('1. Linear Graph ')
    print('2. Pie Chart')
    print('3. Bar Graph')
    print('4. Histogram')
    print('5. Ogive')
    ch = input('Enter your Choice: ')
    if (ch == '1'):
        import LinearGraph
        LinearGraph

    elif (ch == '2'):
        import PieChart
        PieChart

    elif (ch == '3'):
        import BarGraph
        BarGraph
    else:
        print('Please enter a Valid Number')
elif(ch =='2'):
    print('1. Merge Sort ')
    print('2. Quick Sort')
    print('3. Bubble Sort')
    print('4. Insertion Sort')
    print('5. Selection Sort')
    print('6. Heap Sort')
    ch = input('Enter your Choice: ')
    if (ch == '1'):
        import Merge
        Merge

    elif (ch == '2'):
        import Quick
        Quick
    elif (ch == '3'):
        import Bubble
        Bubble
    elif (ch == '4'):
        import Insertion
        Insertion
    elif (ch == '5'):
        import Selection
        Selecion
    elif (ch == '6'):
        import Heap
        Heap
    else:
        print('Please enter a Valid Number')
elif(ch =='3'):
    print('1. Linear Search ')
    print('2. Binary Search')
    print('3. Jump Search')
    print('4. Intrapolation Search')
    print('5. Exponential Search')
    ch = input('Enter your Choice: ')
    if (ch == '1'):
        import LinearS
        LinearS

    elif (ch == '2'):
        import BinaryS
        BinaryS
    elif (ch == '3'):
        import JumpS
        JumpS
    elif (ch == '4'):
        import IntrapolationS
        IntrapolationS
    elif (ch == '5'):
        import ExponentialS
        ExponentialS
    else:
        print('Please enter a Valid Number')
elif (ch =='4'):
    import Statistics
    Statistics



