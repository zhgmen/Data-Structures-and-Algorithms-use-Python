class Weighted_QU(object):

    def __init__(self, maxsize=10):
        self.id = list(range(maxsize))
        self.length = maxsize
        self.sz = []
        for i in range(maxsize):
            self.sz[i] = 1
            
            

    def root(self, i):
        while self.list[i] != i:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]

        return i

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i==j:
            return
        if self.sz[i] < self.sz[j]:
            self.sz[i] = j
            self.sz[j] += self.sz[i]
            self.sz[i] = self.sz[j]
        else:
            
            self.sz[j] = i
            self.sz[i] += self.sz[j]
            self.sz[j] = self.sz[i]

    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    def find(self, i):
        max = i
        while self.list[i] != i:
            i = list[i]
            if i> max:
                max = i
        
        return max
        

