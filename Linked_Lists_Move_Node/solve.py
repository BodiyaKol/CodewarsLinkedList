'''
You have two linked lists, source and dest.
You want to move the first node from source to the front of dest.
'''
class Node(object):
    '''Node class for reference'''
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    '''Context class for reference'''
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    '''Move the first node from source to the front of dest'''
    new_dest = Node(source.data)
    new_source = source.next
    new_dest.next = dest
    return Context(new_source, new_dest)
