'''
You are given a linked list and a number.
You need to insert the number into the list in sorted order.
'''
class Node:
    '''
    A node of a linked list.
    '''
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    '''
    Insert a new node with the given data into the linked list in sorted order.
    '''
    if not head:
        return Node(data)
    new_head = Node(data)
    new_head.next = head
    swapped = True
    while swapped:
        swapped = False
        current = new_head
        while current.next:
            if current.data > current.next.data:
                current.data, current.next.data = current.next.data, current.data
                swapped = True
            current = current.next
    return new_head
