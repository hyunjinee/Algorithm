class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = None


class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            self.count -= 1
            return value
        else:
            print("Queue is empty.")

    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            if self.tail:
                self.tail.pointer = node
            self.tail = node
        self.count += 1

    def size(self):
        # node = self.head
        # num_nodes = 0
        # while node:
        #     num_nodes += 1
        #     node = node.pointer
        # return num_nodes
        return self.count

    def peek(self):
        return self.head.value

    def print(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()


if __name__ == "__main__":
    queue = LinkedQueue()
    print("큐가 비었나요? {0}".format(queue.isEmpty()))
    print("큐에 숫자 0~9를 추가합니다.")
    for i in range(10):
        queue.enqueue(i)
    print("큐가 비었나요? {0}".format(queue.isEmpty()))
    queue.print()

    print("큐 크기: {0}".format(queue.size()))
    print("peek: {0}".format(queue.peek()))
    print("dequeue: {0}".format(queue.dequeue()))
    print("peek: {0}".format(queue.peek()))
    queue.print()