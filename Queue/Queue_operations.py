# This program shows implementation of a Queue data structure


# class to initialize and perform basic queue operations
class Queue:
    # constructor
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    # function to check if a queue is full
    def isFull(self):
        return self.size == self.capacity

    # function to check if a queue is empty
    def isEmpty(self):
        return self.size == 0

    # function to push an item to the queue from rear end
    def enqueue(self, item):
        if self.isFull():
            print("The queue is full, cannot insert an element")
            return
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.Q[self.rear] = item
            self.size += 1
            print("element enqueued is: %s" % str(item))

    # function to pop an item from the front of the queue
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty, cannot dequeue")
            return
        else:
            item = self.Q[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            print("element dequeued is: %s" % str(item))

    # function to get front item in a queue
    def getFront(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("front element is: %s" % str(self.Q[self.front]))

    # function to get rear item in a queue
    def getRear(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("rear element is: %s" % str(self.Q[self.rear]))


if __name__ == '__main__':
    queue = Queue(30)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.dequeue()
    queue.getFront()
    queue.getRear()
