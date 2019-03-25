class Quick_find(object):

    def __init__(self, maxnum = 10):
        self.l = list(range(maxnum))
        self.len = maxnum
        

    def union(self, p, q):
        for i in range(self.len):
            if self.l[q] == self.l[i]:
                self.l[i] = self.l[p]
        

    def conected(self, p, q):
        
        if self.l[p] == self.l[q]:
            return True
        return False
    def find(self, p):
        a = []
        for i in range(self.len):
            if self.l[i] == self.l[p]:
                a.append(self.l[i])
        return a
                


def test():
    pass
quick = Quick_find()
print(quick.get())



        
