# This script inserts a node in the front
# after a given node and at the end of the list


# Creates a new node
class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # Function inserts a new node at the beginning of the linked list
    def insertFront(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function inserts new node after a given node
    def inserAfter(self, new_data, prev_node):
        if prev_node is None:
            print("The given previous node must be in LinkedList.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Function adds a new node to the end of the linked list
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    # Print the linked list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    llist = LinkedList()

    llist.head = Node(6)
    second = Node(4)
    third = Node(9)

    llist.head.next = second
    second.next = third

    llist.insertFront(9)
    llist.insertAfter(2, second)
    llist.append(7)
    llist.append(3)
    llist.printList()
