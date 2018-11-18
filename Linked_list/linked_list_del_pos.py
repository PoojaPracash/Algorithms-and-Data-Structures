# This script deletes the node in the given position


# Class Node creates a node
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    # Delete the node at the given position
    def posDelete(self, position):
        if self.head is None:
            return

        temp = self.head

        # Head has position 0, so delete the head
        if(position == 0):
            self.head = temp.next
            temp = None
            return

        # traverse till the previous position of the given position
        for i in range(position - 1):
            temp = temp.next

        # Check if prev and current position nodes exist in Linked list
        if temp is None:
            return
        elif temp.next is None:
            return

        # If prev n current position nodes exist,
        # link prev node to curr's next node,
        # delete the current position node
        next = temp.next.next
        temp.next = None
        temp.next = next

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)

    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth

    llist.printList()
    llist.posDelete(4)

    print("After deletion")
    llist.printList()
