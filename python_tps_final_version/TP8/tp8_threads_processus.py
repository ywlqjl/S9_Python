from threading import Thread
from multiprocessing import Process
from multiprocessing import Pool
import threading
import time
import os
import random

#1.Tester un calcul (style calcul_long ci-dessous) avec du multi-threading
# et du multi-processing en observant l’utilisation des cœurs de votre CPU.

t = time.time()
def calcul_long():
    print("pid:" + str(os.getpid()))
    n = 1E7
    while n>0:
        n -= 1


    #print("Line cpu", time.time() - t)


# def calcul_long2(threadName, delay, counter):
#     while counter:
# #        if exitFlag:
# #            (threading.Thread).exit()
#         time.sleep(delay)
#         counter -= 1
#         print("%s: %s" % (threadName, time.ctime(time.time())))


def test1_multiThreads():
    try:
       thread.start_new_thread( calcul_long, ("Thread-1", 2, ) )
       thread.start_new_thread( calcul_long, ("Thread-2", 4, ) )
    except:
       print("Error: unable to start thread")

    while 1:
       pass



def test2_multiThreads():
    exitFlag = 0

    class myThread (threading.Thread):   #hériter la class threading.Thread
        def __init__(self, threadID, name, counter):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter
        def run(self):
            print("Starting " + self.name)
            #calcul_long(self.name, self.counter, 10)
            calcul_long()
            print("Exiting " + self.name)


    # Créer nouveaux threads
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)
    thread3 = myThread(3, "Thread-3", 3)
    thread4 = myThread(4, "Thread-4", 4)
    thread5 = myThread(5, "Thread-5", 5)

    # Lancer threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    print("Exiting Main Thread")



# def test1_multiProcessus():
#     with Pool(3) as p:
#         #print(p.map(calcul_long, args=())
#         calcul_long()

def test2_multiProcessus():
    print('Parent process %s.' % os.getpid())

    p = Pool()
    for i in range(5):
    # with Pool(5) as p:
        p.apply_async(calcul_long)
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


# Main
# test2_multiThreads()

test2_multiProcessus()

print("Line cpu", time.time() - t)
