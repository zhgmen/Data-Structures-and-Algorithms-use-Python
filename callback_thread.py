from concurrent.futures import ThreadPoolExecutor
import requests

def fetch_async():
	pass
	
def callback(future):
	print future.result().text
	
url_list = []

pool = ThreadPoolExecutor(10)

for url in url_list:
	v = pool.submit(fetch_async)
	v.add_done_callback(callback)
	
pool.shutdown()