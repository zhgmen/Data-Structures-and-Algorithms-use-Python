'''
def fib():
    a = 0
    b = 1
    while True:
        yield b
        a,b = b,a+b

def simple_coroutine():
    print 'coroutine start'
    x = yield
    print 'coroutine receive [%s]' % x


coroutine = simple_coroutine()
'''
from queue import Queue

class TaskQueue(object):
    _queue =  Queue()

    def __init__():
        pass

    def get_queue():
        return _queue
