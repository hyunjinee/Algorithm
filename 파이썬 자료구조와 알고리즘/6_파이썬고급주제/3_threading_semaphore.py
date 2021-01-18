import threading
import time

class ThreadPool(object):
    def __init__(self):
        self.active = []
        self.lock = threading.Lock()
    
    def acquire(self,name):
        with self.lock:
            self.active.append(name)
            print("획득: {0} | 스레드 풀: {1}".format(name, self.active))
        
    def release(self,name):
        with self.lock:
            self.active.remove(name)
            print("반환: {0} | 스레드 풀: {1}".format(name, self.active))

def worker(semaphore, pool):
    with semaphore:
        name =threading.currentThread().getName()
        pool.acquire(name)
        time.sleep(1)
        pool.release(name)

threads = []
pool = ThreadPool()
semaphore = threading.Semaphore(3)
for i in range(10):
    t = threading.Thread(target=worker, name="스레드 "+str(i) , args=(semaphore, pool))
    t.start()
    threads.append(t)
for t in threads:
    t.join()