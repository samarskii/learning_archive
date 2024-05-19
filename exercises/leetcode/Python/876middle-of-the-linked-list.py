# # Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# class Solution(object):
#     def middleNode(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         node_count = 0
#         if head is not None:
#             print(head.next)
#             node_count += 1
        
#         print(node_count)
#         return
        
        
        
# print(Solution().middleNode(ListNode([1,2,3,4,5])))


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        def append(self, new_node):
            current = self.head
            if current:
                while current.next:
                    current = current.next
                current.next = new_node
            else:
                self.head = new_node
                
            def delete(self, value):
                """Delete the first node with a given value."""
                current = self.head
                if current.value == value:
                    self.head = current.next
                else:
                    while current:
                        if current.value == value:
                            break
                        prev = current
                        current = current.next
                    if current == None:
                        return
                    prev.next = current.next
                    current = None
                
                
e1 = Node(1)
e2 = Node(2)

ll = LinkedList(e1)