class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None:
        raise ValueError()
    first = None
    second = None
    cur1 = first
    cur2 = second
    cur = head
    if head.next.next is None:
        return Context(Node(head.data), Node(head.next.data))
    while cur:
        if first is None and second is None:
            cur1 = cur
            cur2 = cur.next 
            first = cur1
            second = cur2
            cur = cur.next.next
        else:
            cur1.next = cur 
            cur2.next = cur.next if cur.next else None
            cur1 = cur1.next
            cur2 = cur2.next
            cur = cur.next.next if cur.next else None
    cur1.next = None
    if cur2:
        cur2.next = None
    return Context(first, second)
    # Remember to return the context.
