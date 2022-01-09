def bubbleSort(array, drawArray, colours):
    size = len(array)
    for i in range(size-1):
        for j in range(size-i-1):
            if array[j] > array[j+i]:
                array[j], array[j+i] = array[j+i], array[j]
                drawArray(array, [colours[0] if x == j or x == j+1 else colours[1] for x in range(len(array))])

    drawArray(array, [colours[2] for x in range(len(array))])
