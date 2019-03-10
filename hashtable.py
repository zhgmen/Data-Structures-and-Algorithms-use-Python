class Array(object):
    def __init__(self, size , init = None):
        self.size = size
        self._items = [init] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):

        self._items[index] = value

    def __len__(self):
        return len(self._items)
    
    def clear(self,index):
        for index in range(self.size):
            self._items[index] = None

    def __iter__(self):
        for item in self._items:
            if item is not None:
                yield item
        
class Slot(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable(object):
    UNUSED = None
    EMPTY = Slot(None,None)

    def __init__(self):
        self._table = Array(8, init = HashTable.UNUSED)
        self.length = 0

    @property
    def _load_factor(self):
        return self.length / float(len(self._table))

    def __len__(self):
        return self.length

    def _hash(self,key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:
                index = (index*5 + 1) % _len
                continue
            elif self._table[index].key == key:
                return index
            else:
                index = (index*5 + 1) % _len
        return None
    def _find_slot_for_insert(self,key):
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(index):
            
            index = (index*5 + 1) % _len
        return index

    def _slot_can_insert(self, index):
        return (self._table[index] is HashTable.EMPTY or self._table[index] is \
                HashTable.UNUSED)

    def __contains__(self, key):
        index = self._find_key(key)
        return index is not None

    def add(self, key, value):
        if key in self:
            index = self._find_key(key)
            self._table[index].value = value
            return False
        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key,value)
            self.length += 1
            if self._load_factor >= 0.8:
                self._rehash()
            return True
    def _rehash(self):
        old_table = self._table
        newsize = len(self._table)
        self._table = Array(newsize, init=HashTable.UNUSED)
        self.length = 0
        for slot in old_table:
            if self._table[index] is not HashTable.EMPTY or self._table[index] \
               is not HashTable.UNUSED:
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def get(self, key):
        index = self._find_key(key)
        if index is None:
            return None
        else:
            return self._table[index].value

    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise Exception('key not found')
        value = self._table[index].value
        self._table[index] = HashTable.EMPTY
        self.length -= 1
        return value
    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.UNUSED, HashTable.EMPTY):
                yield slot

def test_hash_table():
    h = HashTable()
    h.add('a', 0)
    h.add('b', 1)
    h.add('c', 2)

    assert len(h) == 3
    assert h.get('b') == 1
    assert h.get('d') == None
    

if __name__=='__main__':
    print 'beg',test_hash_table(),'end',
            
            
                
                
