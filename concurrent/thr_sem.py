import threading
import time
sem = threading.Semaphore(2)


def fun1():
    while True:
        sem.acquire()
        print(1)
        time.sleep(0.25)
        sem.release()

        time.sleep(0.25)


def fun2():
    while True:
        sem.acquire()
        print(2)
        time.sleep(0.25)
        sem.release()

        time.sleep(0.25)


def fun3():
    while True:
        sem.acquire()
        print("3 - - - - - 3")
        time.sleep(1)
        sem.release()

        time.sleep(1)


t3 = threading.Thread(target=fun3)
t3.start()

t = threading.Thread(target=fun1)
t.start()
t2 = threading.Thread(target=fun2)
t2.start()