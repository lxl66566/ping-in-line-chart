#coding=utf-8
from ping3 import ping
import matplotlib.pyplot as plt
from math import ceil
from numpy import mean
# import keyboard

a,b,n = {},{},0
_width = 50     #同时显示的ping次数
_pause = 0.45   #ping间隔
_ran = 8        #抖动间隔

plt.ion()
plt.figure(figsize=(9,3),dpi=120)
while 1:

    s = ping("www.baidu.com",timeout=1)
    if(s is None):
        s = 1
    n += 1
    a[n] = ceil(s * 1000)

    if(n >= _width):
        a.pop(n - _width + 1)

    ave = mean(list(a.values()))
    # sta = 0
    # for i in a.values():
    #     if i > ave + _ran:
    #         sta += 1
    # sta = sta / len(a) * 200
    #b[n] = sta


    # if(keyboard.is_pressed('\n') or keyboard.is_pressed('e')):
    #     exit()

    plt.clf()
    plt.plot(a.keys(),a.values() , label='ping')
    plt.plot(a.keys(),[ave] * len(a) , label='average')
    # plt.plot(
    #     [],[],
    #     label = 'instability' + '%.2f' %sta +'%')
    plt.xlabel('times')
    plt.ylabel('ms')
    plt.legend()
    plt.pause(_pause)
    plt.ioff()
