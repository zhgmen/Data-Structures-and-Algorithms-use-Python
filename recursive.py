def factor(n):
    if n == 0:
        return 1
    else:
        
        return n * factor(n-1)
def print_num_recursive(n):
    if n > 0:
        print_num_recursive(n-1)
        print n

def flatten(rec_list):
    for i in rec_list:
        if isinstance(i,list):
            for i in flatten(i):
                yield i
        else:
            yield i
def hannoi_move(n, source, dest, intermediate):
    if n >= 1:
        hannoi_move(n-1, source, intermediate, dest)
        print '%s -> %s' % (source,dest)
        hannoi_move(n-1, intermediate, dest, source)

def test_flatten():
    assert list(flatten([[1,2,[1,2,3]],[1,2,[1,2],3,4]])) == [1,2,1,2,3,1,2,1,2,3,4]
if __name__=='__main__':
    hannoi_move(2,'A', 'B', 'C')


