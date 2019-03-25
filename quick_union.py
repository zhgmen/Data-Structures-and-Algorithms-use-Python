class Quick_Union(object):
    
    def __init__(self, maxnum):
        self.l = list(range(maxnum))
        self.len = len(maxnum)
        
    def root(self, p):
        while self.l[p] != p:
            p = self.l[p]
        
        
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        
        self.l[j] = i

    def connected(self, p, q):
        return self.root(self.l[p]) == self.root(self.l[q])
    
