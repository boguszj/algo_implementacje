def bubble_sort(array):
    for outer_it in range(len(array)):
        for inner_it in range(len(array) - outer_it - 1):
            if array[inner_it] > array[inner_it + 1]: array[inner_it], array[inner_it + 1] = array[inner_it + 1], array[inner_it]
    return array
print(bubble_sort([3,1,5,0]))