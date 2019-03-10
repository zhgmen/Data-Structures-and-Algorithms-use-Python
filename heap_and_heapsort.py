class Array(object):
    def __init__(self, size):
        self.size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        if index >= self.size:
            raise Exception('too large index')
        self._items[index] = value

    def __len__(self):
        return self.size
    def __delitem__(self, index):
        self._items[index] = None

    def clear(self):
        for item in self._items:
            item = None

    def __iter__(self):
        for item in self._items:
            yield item

class MaxHeap(object):
    def __init__(self, maxsize = None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count - 1)
    def _siftup(self, ndx):
        if ndx > 0:
            parent = int((ndx-1)/2)
            if self._elements[parent] < self._elements[ndx]:
                self._elements[parent], self._elements[ndx]= self._elements[ndx], self._elements[parent]
                self._siftup(parent)
    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        del self._elements[self._count]
        self._siftdown(0)
        return value
    def _siftdown(self, ndx):
        left = ndx * 2 + 1
        right = ndx * 2 + 2
        largest = ndx
        if left <= self._count and self._elements[left] >= self._elements[largest]\
           and self._elements[left] >= self._elements[right]:
            largest = left
            
        elif right <= self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        if largest != ndx:
            self._elements[largest], self._elements[ndx] = self._elements[ndx], self._elements[largest]
            self._siftdown(largest)
def heapsort_reverse(array):
    length = len(array)
    maxheap = MaxHeap(length)
    for i in array:
        maxheap.add(i)
    return [maxheap.extract() for i in range(length)]
def heapsort_use_heapq(iterable):
    from heapq import heappush, heappop
    items = []
    for value in iterable:
        heappush(items,i)
    return [heappop(items) for i in range(len(items))]
def test_maxheap():
    import random
    n = 5
    h = MaxHeap(n)
    for i in range(n):
        h.add(i)
    for i in reversed(range(n)):
        assert i == h.extract()     
