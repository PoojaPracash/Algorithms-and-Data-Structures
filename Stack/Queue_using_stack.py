# This program shows implementation of a Queue using stack(linked list)


# class to define a node structure
class StackNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    # checks if stack is empty
    def isEmpty(self):
        return True if self.head is None else False

    # push an element to a stack
    def push(self, new_data):
        new_node = StackNode(new_data)
        new_node.next = self.head
        self.head = new_node
        print("%d pushed" % (new_data))

    # pop an element from a stack
    def pop(self):
        if(self.isEmpty()):
            return float("-inf")
        temp = self.head
        self.head = self.head.next
        pop_data = temp.data
        return pop_data

    # Peek at the top of a stack__
    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.head.data


class Queue:

    # Initialize input queue & output queue as empty stacks
    def __init__(self):
        self.inQ = Stack()
        self.outQ = Stack()

    # Function to check if queue is empty
    def isEmpty(self):
        return (self.inQ.isEmpty() and self.outQ.isEmpty())

    # Function to push/enqueue item into queue
    def enQueue(self, data):
        self.inQ.push(data)

    # Function to pop/dequeue item from queue
    def deQueue(self):
        if self.outQ.isEmpty():
            while not self.inQ.isEmpty():
                popped = self.inQ.pop()
                self.outQ.push(popped)
        return self.outQ.pop()


if __name__ == '__main__':
    queue = Queue()
    while True:
        print('1.enqueue')
        print('2.dequeue')
        print('3.quit')
        do = input('What would you like to do(Enter number)?')

        operation = do
        if operation == '1':
            item = int(input("Enter an item to enqueue:"))
            queue.enQueue(item)
        elif operation == '2':
            if queue.isEmpty():
                print('Queue is empty.')
            else:
                dequeued = queue.deQueue()
                print('Dequeued element: ', int(dequeued))
        elif operation == '3':
            break
        else:
            print("No operation match")
            break
