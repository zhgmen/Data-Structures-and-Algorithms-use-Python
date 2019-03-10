from collections import defaultdict, OrderedDict


class Node:
    __slots__ = 'key', 'val', 'cnt'

    def __init__(self, key, val, cnt=0):
        self.key = key
        self.val = val
        self.cnt = cnt

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.cnt2node = defaultdict(OrderedDict)
        self.mincut = 0

    def get(self, key, default=-1):
        if key not in self.cache:
            return default
        node = self.cache[key]
        del self.cnt2node[node.cnt][key]
        if not self.cnt2node[node.cnt]:
            del self.cnt2node[node.cnt]

        node.cnt += 1
        self.cnt2node[node.cnt][key] = node

        if not self.cnt2node[self.mincut]:
            self.mincut += 1
        return node.val
    def put(self, key, value):
        if key in self.cache:
            self.cache[key].val = value
            self.get(key)
            return
        if len(self.cache) >= self.capacity:
            pop_key, _pop_node = self.cnt2node[self.mincut].popitem(last=False)
            del self.cache[pop_key]

        self.cache[key] = self.cnt2node[1][key] = Node(key, value, 1)
        self.mincut = 1
def test_lfucache():
    c = LFUCache(2)
    c.put(1,2)
    c.put(2,2)
    assert c.get(1) == 2
    c.put(3,3)
    assert c.get(2) == -1
    assert c.get(3) == 3
    c.put(4,4)
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4
    
test_lfucache() 
