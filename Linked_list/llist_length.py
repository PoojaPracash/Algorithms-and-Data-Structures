# This script finds the length of the linked list iteratively


# creates a new node
class Node():
    def __init__(self, data):
        self.data = None
        self.next = None


class linkedList():
    # Function initializes the head
    def __init__(self, head=None):
        self.head = head

    # get length of the linked list
    def getLength(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next
        return count

    # This function counts number of nodes in Linked List
    # recursively, given 'node' as starting node.
    def getCountRec(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.getCountRec(node.next)

    # A wrapper over getCountRec()
    def getCount(self):
        return self.getCountRec(self.head)

    def push(self, new_data):
        # Allocate the Node & put in the data
        new_node = Node(new_data)
        # Make next of new Node as head
        new_node.next = self.head
        # Move the head to point to new Node
        self.head = new_node


if __name__ == '__main__':
    llist = linkedList()
    llist.push(1)
    llist.push(3)
    llist.push(2)
    llist.push(7)
    print("Length of linked list is(iteratively):", llist.getLength())
    print("Length of linked list is(recursively):", llist.getCount())
