'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Node:
    '''
    A node of a linked list.
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    '''
    Push a new node with the given data to the front of the linked list.
    '''
    if head is None:
        return Node(data)
    new_head = Node(data)
    new_head.next = head
    return new_head

def build_one_two_three():
    '''
    Build a linked list with three nodes containing data 1, 2, and 3.
    '''
    head = None
    prev_cur = None
    for i in range(3):
        cur = Node(i+1)
        if i == 0:
            head = cur
            prev_cur = cur
        else:
            prev_cur.next = cur
            prev_cur = cur
    return head
