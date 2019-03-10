class Array(object):
    def __init__(self,size):
        self.size = size
        self._items = [None] * size

    def __getitem__(self,index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return len(self._items)

    def clear(self):
        for i in range(self.__len__()):
            self._items[i] = None

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
        # is full?
        self.array[head] = value
        self.head += 1
        

    def pop(self):
        value = array[self.tail]
        self.tail += 1
        return value

    def __len__(self):
        return self.head - self.tail

class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
        
class Linkedlist(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        if maxsize is not None and len(self) >= self.maxsize:
            raise Exception('Linkedlist is full')
        node = Node(value)
        tailnode = self.tailnode
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node
        self.length += 1
        
    def appendleft(self,value):
        node = Node(value)
        if self.tailnode is None:
            self.tailnode = node
            self.length += 1
        else:
            headnode = self.root.next
            self.root.next = node
            node.next = headnode
            self.length += 1
            
    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        if curnode is not None:
            yield curnode

    def remove(self,value):
        
        
        
