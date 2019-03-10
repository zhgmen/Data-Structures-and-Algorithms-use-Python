from collections import OrderedDict
from functools import wraps

def cache(func):
	store = {}
	@wraps(func)
	def _(n):
		if n in store:
			return store[n]
		else:
			res = func(n)
			store[n] = res
			return res
	return _
@cache
def f(n):
	if n <= 1:
		return n
	return f(n-1) + f(n-2)
class LRUCache(object):

	def __init__(self, capacity=128):
		self.capacity = capacity
		self.od = OrderedDict()

	def get(self, key, default=None):
		val = self.od.get(key,default)
		self.od.move_to_end(key)
		return val

	def add_or_update(self, key, value):
		if key in self.od:
			self.od[key] = value
			self.od.move_to_end(key)
		else:
			self.od[key] = value
			if len(self.od) > self.capacity:
				self.od.popitem(last=False)

	def __call__(self, func):
		@wraps(func)
		def _(n):
			if n in self.od:
				return self.get(n)
			else:
				val = func(n)
				self.add_or_update(n, val)
				return val
		return _
@LRUCache(10)
def fib_use_lru(n):
	if n <= 1:
		return n
	return fib_use_lru(n-1) + fib_use_lru(n-2)
def test():
	import time
	beg = time.time()
	for i in range(34):
		print(f(i))
	print(time.time()-beg)
	print(f.__name__)
	beg = time.time()
	for i in range(34):
		print(fib_use_lru(i))
	print(time.time()-beg)
	print(fib_use_lru.__name__)

test()
