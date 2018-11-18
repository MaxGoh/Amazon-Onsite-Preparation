class CircularQueue:
    """ Queue : FIFO """
    def __init__(self, capacity):
        self.queue = [0] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = capacity

    def push(self, val):
        """
        Time Complexity: O(1)
        Space Complexity: O(1)

        :param val: int
        :return: None
        """
        if self.size > self.capacity:
            print("Queue is full")
            return

        self.queue[self.tail] = val
        self.size += 1
        self.tail += 1

    def pop(self):
        """
        Time Complexity: O(1)
        Space Complexity: O(1)

        :return:
        """
        if self.head == self.tail and self.size == 0:
            print("Queue is empty")
            return

        self.queue[self.head] = 0
        self.size -= 1
        self.head += 1

    def get_size(self):
        """
        Time Complexity: O(1)
        Space Complexity: O(1)

        :return: None
        """
        print(self.size)

    def print(self):
        print(self.queue)


if __name__ == "__main__":
    cq = CircularQueue(5)

    cq.push(5)
    cq.push(1)
    cq.push(3)

    cq.print()

    cq.pop()

    cq.print()
    cq.pop()
    cq.print()
    cq.get_size()