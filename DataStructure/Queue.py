from collections import deque


class Queue:
    """ Queue : FIFO """

    def __init__(self):
        self.queue = deque()
        self.size = 0

    def push(self, val):
        self.queue.appendleft(val)
        self.size += 1

    def pop(self):
        self.queue.popleft()
        self.size -= 1

    def print(self):
        print(self.queue)
        for elem in self.queue:
            print(elem)


if __name__ == "__main__":
    q = Queue()
    q.push(5)
    q.push(4)
    q.push(3)
    q.print()
    q.pop()
    q.print()

