from collections import deque


queue = deque()


queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# deque객체를 리스트 자료형으로 변경하고자 한다면 list()메서드를 활용한다.
# list(queue) 를 하면 리스트 자료형이 반환된다.


