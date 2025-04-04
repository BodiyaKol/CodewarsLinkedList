'''loop function'''
def loop_size(node):
    '''
    Determines the size of the loop in a linked list.
    '''
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            count = 1
            current = slow.next
            while current != slow:
                current = current.next
                count += 1
            return count
    return 0
