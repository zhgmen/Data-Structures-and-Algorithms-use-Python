import requests
import threading
from Queue import Queue
import time
import random
import json
import os
import urllib

IMG_SRC = 'C:\Users\Meng\Desktop\Splash'
url_queue = Queue()
THREAD_NUM = 4

class Splash(threading.Thread):
    NOT_EXIST = 0
    def __init__(self,thread_id):
        threading.Thread.__init__(self)
        thread_id = thread_id
        
    def run(self):
        while not self.NOT_EXIST:
            if url_queue.empty():
                break
            url = url_queue.get()
            self.get_data(url)
            time.sleep(random.randint(3,5))
            
            
            

    def get_data(self,url):
        headers = {
            
            'User-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.3\
6 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,\
image/webp,image/apng,*/*;q=0.8',
            'referer': 'https://unsplash.com/',
            'path': url.split('com')[1],
            'authority': 'unsplash.com',
            'viewport-width': '1920',

            }
        response = requests.get(url,headers = headers)
        
        self.get_image_url(response.text)
        
    def get_image_url(self,response):
        img_url = json.loads(response)[0]['urls']['full']
        self.save_img(img_url)
        

    def save_img(self,img_url):
        print img_url
        
        if not os.path.exists(IMG_SRC):
            os.mkdir(IMG_SRC)

        filename = IMG_SRC+img_url.split('com/')[1].split('?')[0]
        urllib.urlretrieve(img_url,filename)
        
        
            
        


def get_all_url():
    base_url = 'https://unsplash.com/napi/photos?page={}&per_page=1&order_by=\
latest'
    page = 1
    max_page = 10
    while page <= max_page:
        url = base_url.format(page)
        url_queue.put(url)
        page += 1
        
        

if __name__ == '__main__':
    get_all_url()
    for i in range(THREAD_NUM):
        splash = Splash(i)
        splash.start()
    
