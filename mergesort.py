def mergesort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left_side_array = array[:middle]
        right_side_array = array[middle:]
        
        mergesort(left_side_array)
        mergesort(right_side_array)
        
        left_array_iterator = 0
        right_array_iterator = 0
        array_iterator = 0
        
        while left_array_iterator < len(left_side_array) and right_array_iterator < len(right_side_array):
            if left_side_array[left_array_iterator] < right_side_array[right_array_iterator]:
                array[array_iterator] = left_side_array[left_array_iterator]
                left_array_iterator += 1
            else:
                array[array_iterator] = right_side_array[right_array_iterator]
                right_array_iterator += 1
            array_iterator += 1
            
        while left_array_iterator < len(left_side_array):
            array[array_iterator] = left_side_array[left_array_iterator]
            left_array_iterator += 1
            array_iterator += 1
            
        while right_array_iterator < len(right_side_array):
            array[array_iterator] = right_side_array[right_array_iterator]
            right_array_iterator += 1
            array_iterator += 1
        
        return array
    
# ITERATIVE IMPLEMENTATION
    
def iterative_mergesort(array):
    current_size = 1
    while current_size < len(array) - 1:
        left = 0
        while left < len(array) - 1:
            middle = left + current_size - 1
            right = min(left + 2 * current_size, len(array)) - 1
            merge(array, left, middle, right)
            left += 2 * current_size
        current_size *= 2
    return array
    
def merge(array, left, middle, right):
    n_left = middle - left + 1
    n_right = right - middle
    left_array = [None] * n_left
    right_array = [None] * n_right
    for it in range (n_left): left_array[it] = array[left + it]
    for it in range (n_right): right_array[it] = array[middle + it + 1]
    left_it = 0
    right_it = 0
    array_it = left
    while left_it < n_left and right_it < n_right:
        if left_array[left_it] < right_array[right_it]:
            array[array_it] = left_array[left_it]
            left_it += 1
        else:
            array[array_it] = right_array[right_it]
            right_it += 1
        array_it += 1
        
    while left_it < n_left:
        array[array_it] = left_array[left_it]
        left_it += 1
        array_it += 1
    
    while right_it < n_right:
        array[array_it] = right_array[right_it]
        right_it += 1
        array_it += 1
        
print(mergesort([1, 3, 0, 5, 1, 9, 33, 1]))
print(iterative_mergesort([1, 3, 0, 5, 1, 9, 33, 1]))