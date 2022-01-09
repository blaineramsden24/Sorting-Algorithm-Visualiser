import time


def bubble_sort(array, drawArray, timeTick = 0.5):
    size = len(array)
    for i in range(size-1):
        for j in range(size-i-1):
            if array[j] > array[j+i]:
                array[j], array[j+i] = array[j+i], array[j]
                drawArray(array, ['#05F50E' if x == j or x == j+1 else '#F22810' for x in range(len(array))])

    drawArray(array, ['#FFFFFF' for x in range(len(array))])
