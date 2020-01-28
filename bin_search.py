def bin_search(array, value):
    start = 0
    end = len(array) - 1
    while start <= end:
        middle = start + (end - start) // 2
        if array[middle] < value:
            start = middle + 1
        elif array[middle] > value:
            end = middle - 1
        else: return middle
    return -1

print(bin_search([1,3,7,9], 9))