class Bag(object):
    def __init__(self,maxsize = 10):
        self.maxsize = maxsize
        self._items = list()

    def add(self,item):
        if len(self) >= self.maxsize:
            raise Exception('full')
        self._items.append(item)

    def remove(self,item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item

bag = Bag()
bag.add('s')
