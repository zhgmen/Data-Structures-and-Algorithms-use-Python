from hashtable import HashTable

class DictADT(HashTable):

    def __setitem__(self, key, value):
        self.add(key,value)

    def __getitem__(self, key):
        if key not in self:
            raise Exception('None')
        else:
            
            return self.get(key)
    '''
    def _iter_slot(self):
        for slot in self._table:
            if slot is not 
            yield slot
            
    '''
    
    def items(self):
        for slot in self.__iter__():
            yield (slot.key,slot.value)

    def keys(self):
        for slot in self.__iter__():
            yield slot.key
    def values(self):
        for slot in self.__iter__():
            yield slot.value

def test_dict_adt():
    pass
    

            
