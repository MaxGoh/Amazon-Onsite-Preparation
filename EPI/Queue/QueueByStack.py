# Implement a Queue using Stacks
# Queue - FIFO | Stack - LIFO


class Queue:
    def __init__(self, capacity):
        self.enq = []
        self.deq = []

    def enqueue(self, val):
        self.enq.append(val)

    def dequeue(self):
        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())
            return self.deq.pop()