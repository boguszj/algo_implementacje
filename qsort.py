def quicksort(array):
	return qsort(array, 0, len(array) - 1)

def qsort(array, left, right):
	if left < right:
		division_index = devide(array, left, right)
		qsort(array, left, division_index - 1)
		qsort(array, division_index + 1, right)
	return array

def swap(array, a, b):
	tmp = array[a]
	array[a] = array[b]
	array[b] = tmp
	return array

def devide(array, left, right):
	middle = int(left + (right - left) / 2)
	array = swap(array, middle, right)
	current = left
	for it in range(left, right):
		if array[it] < array[right]:
			array = swap(array, current, it)
			current += 1
	array = swap(array, right, current)
	return current

# ITERATIVE IMPLEMENTATION

def iterative_quicksort(array):
    stack = []
    stack.append(0)
    stack.append(len(array) - 1)
    while stack:
        right = stack.pop()
        left = stack.pop()
        
        partition_point = devide(array, left, right)
        
        if partition_point - 1 > left:
            stack.append(left)
            stack.append(partition_point - 1)
        if partition_point + 1 < right:
            stack.append(partition_point + 1)
            stack.append(right)
    return array    

print(quicksort([3,1,5,8,2,1]))
print(iterative_quicksort([3,1,5,8,2,1]))