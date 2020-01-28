def insort(array):
    for idx in range(1, len(array)):
        current_position = idx
        saved_value = array[idx]
        while current_position > 0 and array[current_position - 1] > saved_value:
            array[current_position] = array[current_position - 1]
            current_position -= 1
        array[current_position] = saved_value
    return array

print(insort([3, 12, 0, 1, 14]))