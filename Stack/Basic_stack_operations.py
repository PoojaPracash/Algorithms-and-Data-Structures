# This program shows implementation of a stack using python list
from sys import maxsize


# Function to create a stack.
def createStack():
    stack = []
    return stack


# Function to check if a stack is empty
def isEmpty(stack):
    return len(stack) == 0


# Function to push an item to stack
def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack")
    return stack


# Function to pop an item from a stack
def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize - 1)

    return stack.pop()


if __name__ == '__main__':
    stack = createStack()
    push(stack, str(3))
    push(stack, str(2))
    push(stack, str(1))
    print("Element " + pop(stack) + " popped from stack")
