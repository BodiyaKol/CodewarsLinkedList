'''
Convert a linked list to a string
'''
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
        current = current.next
    values_list.append('None')
    return ' -> '.join(values_list)
