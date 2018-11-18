# This script deletes the complete linked list created


# Class Node will create a node
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    # Function to delete linked list
    def deleteList(self):
        # Start with head of the list
        current = self.head

        # While the linked list have head, find next, delete current
        # and make next as current
        while current:
            prev = current.next
            del current.data
            current = prev

    # Function to print the linked list
    def printList(self):
        # Start with head of the list
        temp = self.head

        # While head exist, print value and check next node existence
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    # Create an object llist
    llist = LinkedList()

    # Create nodes
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Link all the created nodes
    llist.head.next = second
    second.next = third

    llist.printList()
    llist.deleteList()
    llist.head = Node(1)
    llist.printList()
