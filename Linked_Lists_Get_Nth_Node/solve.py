'''
Gets nth node from a linked list.
'''
class Node:
    """Node class for reference"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def get_nth(node, index):
    '''
    Get the nth node from a linked list.
    '''
    cur = node
    i=0
    nth_node = None
    while cur:
        if i == index:
            nth_node = cur
        i+=1
        cur = cur.next
    if nth_node:
        return nth_node
    raise IndexError()
    # Your code goes here.
