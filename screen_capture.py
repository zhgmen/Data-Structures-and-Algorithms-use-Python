# -*- coding=utf-8 -*-

from PIL import ImageGrab
import random



def img_get_name():# 获取随机字符作为文件名
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    filename = ''.join(random.choice(seed) for _ in range(6))
    return filename + '.jpg'

def capturer(x, y, w, h):
    x1 = x + w
    y1 = y + h
    if x >= x1 or y >= y1:# 图片大小不合格
        raise Exception('error size')
    img_box = (x, y, x+w, y+h)    
    img = ImageGrab.grab(bbox=img_box)# 截屏
    img_name = img_get_name()
    img.save(img_name)# 保存图片到当前路径
    return img_name


if __name__ == '__main__':
    x, y = input('inter Starting point coordinates such as： x, y:') 
    w, h = input('inter width and height such as w, h:')
    print capturer(x, y, w, h)
    
