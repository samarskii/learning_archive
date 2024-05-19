class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
       
       
list1 = ListNode(1, ListNode(2, ListNode(4)))

print(list1.val)