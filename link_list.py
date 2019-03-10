

class Node(object):
    
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return '<Node: value: {}, next: {}>'.format(self.value, self.next)


class LinkedList(object):

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self,value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
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
        prenode = self.root
        for curnode in self.iter_node():
            if curnode.value == value:
                prenode.next = curnode.next
                if curnode is self.tailnode:
                    self.tailnode = prenode
                del curnode
                self.length -= 1
                return 1
            else:
                prenode = curnode
        return -1

    def find(self,value):
        index = 0
        for curnode in self.iter_node():
            if curnode.value == value:
                return index
            index += 1
        return -1

    def popleft(self):
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value
        if self.tailnode is headnode:
            self.tailnode = node
        del headnode
        return value

    def clear(self):
        for node in iter_node(self):
            del node
        self.root.next = None
        self.length = 0
        self.tailnode = None

    def reverse(self):
        curnode = self.root.next
        self.tailnode = curnode
        prenode = Node
        while curnode:
            nextnode = curnode.next
            curnode.next = prenode
            if nextnode is None:
                self.root.next = curnode
            prenode = curnode
            curnode = nextnode

            
