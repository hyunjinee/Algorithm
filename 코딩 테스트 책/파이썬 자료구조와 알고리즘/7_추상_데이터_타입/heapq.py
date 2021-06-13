# heapq 모듈은 효율적으로 시퀀스를 힙으로 유지하면서 항목을 삽입하고 제거하는함수를 제공한다. 다음과같이 heapq.heapify함수를 사용하면 
# n 시간에 리스트를 힙으로 변환가능.


class Heapify(object):
    def __init__(self, data=None):

        self.data = data or []

        for i in range(len(data)// 2 , -1, -1):
            self.__max_heapify__(i)

    def __repr__(self):
        return repr(self.data)

    def parent(self, i):
        if i & 1:
            