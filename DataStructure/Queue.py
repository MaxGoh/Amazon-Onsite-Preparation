from collections import deque


class Queue:
    """ Queue : FIFO """

    def __init__(self):
        self.queue = deque()
        self.size = 0

    def enqueue(self, val):
        self.queue.append(val)
        self.size += 1

    def dequeue(self):
        self.queue.popleft()
        self.size -= 1

    def print(self):
        print(self.queue)
        for elem in self.queue:
            print(elem)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(4)
    q.enqueue(3)
    q.print()
    q.dequeue()
    q.print()

