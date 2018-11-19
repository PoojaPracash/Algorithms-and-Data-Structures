# This script will create a circular linked list and will traverse the list


# Class Node will create an Node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class circularLinkedList:
    # constructor to create an empty linked list
    def __init__(self):
        self.head = None

    # function to create a circular linked list
    def push(self, data):
        # create a node
        new_node = Node(data)
        # save the head node
        temp = self.head

        # point new node next to head of the linked list
        new_node.next = self.head

        # Check if linked list is not empty
        if self.head is not None:
            # Traverse through the linked list to the last element
            # last node's next is pointed to the head of the linked list
            while(temp.next != self.head):
                temp = temp.next
            # one you reach last node, point it's next to new node
            temp.next = new_node
        else:
            # If linked list is empty,
            # point new node's next to new node
            new_node.next = new_node

        self.head = new_node

    # Function to print the circular linked list nodes
    def printList(self):
        temp = self.head

        if self.head is not None:
            while(True):
                print("%d" % (temp.data))
                temp = temp.next
                if temp == self.head:
                    break


if __name__ == '__main__':
    # Initialize linked list as empty
    cllist = circularLinkedList()
    cllist = cllist.push(1)
    cllist = cllist.push(6)
    cllist = cllist.push(3)
    cllist = cllist.push(9)

    cllist.printList()
