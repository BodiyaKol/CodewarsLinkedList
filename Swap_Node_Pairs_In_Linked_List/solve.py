class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head
    new_head = head.next
    prev = None
    cur = head
    while cur and cur.next:
        first = cur
        second = cur.next
        first.next = second.next
        second.next = first
        if prev:
            prev.next = second
        prev = first
        cur = first.next
    return new_head
