#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time
import detect1
import takeoff

class myThread0 (threading.Thread):   #继承父类threading.Thread  此线程负责运行视觉处理数据
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        detect1.main()


class myThread1 (threading.Thread):   #继承父类threading.Thread1  此线程负责控制无人机并提取视觉处理数据
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        takeoff.main()
        

def run():
    thread1 = myThread0()
    thread2 = myThread1()
    thread1.start()
    time.sleep(6)
    thread2.start()
if __name__ == '__main__':
    run()
