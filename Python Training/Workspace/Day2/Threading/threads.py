from threading import Thread
import time

class MyThread(Thread):
    def __init__(self, threadName):
        Thread.__init__(self, name = threadName)
        
        
    def run(self):
        for val in range(0,4):
            print('---Inside run: ', self.getName())
            time.sleep(1)
        
threadObj = MyThread('\nFirstThread')
threadObj.start()

threadObj1 = MyThread('\nSecondThread')
threadObj1.start()