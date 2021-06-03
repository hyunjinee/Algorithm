import threading

def consumer(cond):
    name = threading.currentThread().getName()
    print("{0} 시작".format(name))
    with cond:
        print("{0} 대기".format(name))
        cond.wait()
        print("{0} 자원소비".format(name))


def producer(cond):
    name = threading.currentThread().getName()
    print("{0} 시작".format(name))
    with cond:
        print("{0} 자원 생산 후 모든 소비자에게 알림".format(name))
        cond.notifyAll()
    
condition = threading.Condition()
consumer1 = threading.Thread(name="소비자1", target=consumer, args= (condition,))
consumer2 = threading.Thread(name="소비자2", target=consumer, args= (condition,))
producer = threading.Thread(name="생산자", target=producer, args=(condition,))

consumer1.start()
consumer2.start()
producer.start()