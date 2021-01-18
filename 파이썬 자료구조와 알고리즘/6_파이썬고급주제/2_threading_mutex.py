from threading import Thread, Lock
import threading

def worker(mutex, data, thread_safe):
    if thread_safe:
        mutex.acquire()
    try:
        print("스레드 {0}: {1}\n".format(threading.get_ident(),data))
    finally:
        if thread_safe:
            mutex.release()


threads = []
thread_safe= True
mutex = Lock()
for i in range(20):
    t = Thread(target=worker, args=(mutex, i, thread_safe))
    t.start()
    threads.append(t)
for t in threads:
    t.join()