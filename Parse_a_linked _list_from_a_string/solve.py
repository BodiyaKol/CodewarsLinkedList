class Node:
    '''
    A node of a linked list.
    '''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


def linked_list_from_string(s):
    '''
    Create a linked list from a string representation.
    '''
    nodes=s.split(' -> ')
    nodes = [Node(int(el)) if el != 'None' else None for el in nodes]
    head = nodes[0]
    for i,node in enumerate(nodes[1:]):
        i+=1
        nodes[i-1].next = node 
    return head

print(linked_list_from_string('0 -> 1 -> 2 -> 3 -> None'))
