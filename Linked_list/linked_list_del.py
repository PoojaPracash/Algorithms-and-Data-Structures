# This script deletes a particular given node from a linked list


# Class to create a node
class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    # Deletes a particular node with given key
    def deleteNode(self, key):
        # Start with head of the list
        temp = self.head

        # Check if head/node exist
        while temp is not None:
            # If match key is found, link present node to next node
            # and delete matching key node
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
            break

        # Ckeck if head/node exist
        while temp is not None:
            # If match key not found, save present node, check next node value
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return "Key not present"

        # If key to be deleted is found, link prev node to next node
        # delete the key
        prev.next = temp.next
        temp = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    llist.head.next = second
    second.next = third
    third.next = fourth
    print("Before Deletion")
    llist.printList()

    llist.deleteNode(1)
    llist.deleteNode(3)
    llist.deleteNode(5)

    print("After Deletion")
    llist.printList()
