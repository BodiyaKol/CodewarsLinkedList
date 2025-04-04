'''
Convert a linked list to a string
'''
class Node:
    '''
    A node of a linked list.
    '''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def stringify(node):
    '''
    Convert a linked list to a string representation.
    '''
    if node is None:
        return 'None'
    values_list = [str(node.data)]
    current = node.next
    while current:
        values_list.append(str(current.data))
        current = next.next
    values_list.append('None')
    return ' -> '.join(values_list)
