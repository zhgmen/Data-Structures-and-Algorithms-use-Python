from array import array


class Array(object):
    
    def __init__(self,size=32):
        self.size = size
        self._items = [None] * size

    def __getitem__(self,index):
        return self._items[index]

    def __setitem__(self,index,value):
        self._items[index] = value

    def __len__(self):
        return len(self._items)

    def clear(self,value=None):
        for i in range(len(self._items)):
            self.items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item
class ArrayQueue(object):
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0
    def push(self,value):
        self.array[head] = value
        self.head += 1
    
    def pop(self):
        value = self.array[self.tail]
        self.tail += 1
        return value
    
    def __len__(self):
        return self.head - self.tail
