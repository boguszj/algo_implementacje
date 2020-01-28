class MinHeap:
    def __init__(self, array = []):
        self.heap_array = array
        self.size = len(array)
        self.build_min_heap()
                
    def build_min_heap(self):
        if self.size > 0:
            for it in range(self.size // 2, -1, -1):
                self.heapify_down(it)
        
    def get_parent_index(self, idx):
        return (idx - 1) // 2
    
    def get_right_child_index(self, idx):
        return idx * 2 + 2
    
    def get_left_child_index(self, idx):
        return idx * 2 + 1
    
    def get_right_child_value(self, idx):
        return self.heap_array[self.get_right_child_index(idx)]
    
    def get_left_child_value(self, idx):
        return self.heap_array[self.get_left_child_index(idx)]
    
    def get_parent_value(self, idx):
        return self.heap_array[self.get_parent_index(idx)]
    
    def has_left_child(self, idx):
        return self.get_left_child_index(idx) < self.size
    
    def has_right_child(self, idx):
        return self.get_right_child_index(idx) < self.size
    
    def has_parent(self, idx):
        return self.get_parent_index(idx) >= 0
    
    def get_index_value(self, idx):
        return self.heap_array[idx]
    
    def swap(self, first_idx, second_idx):
        self.heap_array[first_idx], self.heap_array[second_idx] = self.heap_array[second_idx], self.heap_array[first_idx]
    
    def heapify_up(self, idx):
        if self.has_parent(idx) and self.get_parent_value(idx) > self.get_index_value(idx):
            self.swap(idx, self.get_parent_index(idx))
            self.heapify_up(self.get_parent_index(idx))
            
    def heapify_down(self, idx):
        subroot_index = idx
        subroot_value = self.get_index_value(idx)
        
        if self.has_left_child(idx) and self.get_left_child_value(idx) < subroot_value:
            subroot_index = self.get_left_child_index(idx)
            subroot_value = self.get_left_child_value(idx)
            
        if self.has_right_child(idx) and self.get_right_child_value(idx) < subroot_value:
            subroot_index = self.get_right_child_index(idx)
            
        if idx != subroot_index:
            self.swap(idx, subroot_index)
            self.heapify_down(subroot_index)

    def put(self, value):
        self.size += 1
        self.heap_array.append(value)
        self.heapify_up(self.size - 1)
        
    def pop(self):
        if self.size == 0: raise Exception('Cannot pop from empty heap')
        self.swap(0, self.size - 1)
        self.size -= 1
        result = self.heap_array.pop()
        if self.heap_array: self.heapify_down(0)
        return result
    
    def sort(self):
        saved_size = self.size
        for it in range(self.size - 1, -1, -1):
            self.swap(0, it)
            self.size -= 1
            self.heapify_down(0)
        self.size = saved_size
    
    def get_at_index(self, idx):
        if idx >= self.size or idx < 0: raise Exception('No such index in heap')
        if idx == self.size - 1:
            self.size -= 1
            return self.heap_array.pop()
        self.swap(idx, self.size - 1)
        result = self.heap_array.pop()
        self.size -= 1
        if self.has_parent(idx) and self.get_parent_value(idx) > self.get_index_value(idx):
            self.heapify_up(idx)
        else:
            self.heapify_down(idx)
        return result
        
    
print('---------put, pop, delete----------')    
h = MinHeap([11,9,10])
h.put(1)
h.put(0)
h.put(7)
h.put(2)
h.put(4)
h.put(1)
h.put(5)
print(h.heap_array)
print('pop ', h.pop())
print('pop ', h.pop())
print('pop ', h.pop())
print('pop ', h.pop())
print('pop ', h.pop())
print(h.heap_array)
print(h.get_at_index(4))
print(h.heap_array)
print('pop ', h.pop())
print('pop ', h.pop())
print('pop ', h.pop())
print('pop ', h.pop())
print(h.heap_array)

print('----------sort----------')
h = MinHeap([11,9,10])
h.put(1)
h.put(0)
h.put(7)
h.put(2)
h.put(4)
h.put(1)
h.put(5)
print(h.heap_array)
print('pop ', h.pop())
print('pop ', h.pop())
print('pop ', h.pop())
print('pop ', h.pop())
h.sort()
print(h.heap_array)