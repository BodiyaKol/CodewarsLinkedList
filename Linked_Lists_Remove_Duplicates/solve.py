class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None
    prev_cur = head
    cur = head.next
    while cur:
        if prev_cur.data == cur.data:
            prev_cur.next = cur.next
            cur = cur.next
        else:
            prev_cur = cur
            cur = cur.next
    return head
    # Remember to return the head of the list.
