# This program shows implementation of a Stack using linked list


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
        print("%d pushed to stack" % (new_data))

    # pop an element from a stack
    def pop(self):
        if(self.isEmpty()):
            return float("-inf")
        temp = self.head
        self.head = self.head.next
        pop_data = temp.data
        return pop_data

    # Peek at the top of a stack
    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.head.data


if __name__ == '__main__':
    stack = Stack()
    stack.push(3)
    stack.push(5)
    stack.push(1)
    print("%d popped from stack" % (stack.pop()))
    print("Top element is %d " % (stack.peek()))
