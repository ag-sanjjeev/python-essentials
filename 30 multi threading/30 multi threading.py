# multi threading
from time import sleep
from threading import *


class process1(Thread):
    def run(self):  # this is default function for thread process
        for i in range(10):
            print("Process 1")
            sleep(1)  # avoid thread collision


class process2(Thread):
    def run(self):
        for i in range(10):
            print("Process 2")
            sleep(1)  # avoid thread collision


p1 = process1()
p2 = process2()

p1.start()
sleep(0.5)  # avoid thread collision
p2.start()
p1.join()  # to wait main thread until threads are finishing execution
p2.join()
print("Main Thread Executes")