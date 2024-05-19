class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        
print(Solution().addTwoNumbers([2,4,3], [5,6,4]))
print(Solution().addTwoNumbers([0], [0]))
print(Solution().addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))


# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         def reverse (item, tail = None):
#             next = item.next
#             item.next = tail
#             if next is None:
#                 return item
#             else:
#                 return reverse(next, item)
        
#         print(l1)
#         print(l2)
#         l1_new = list()
#         l2_new = list()
#         reverse(l1)
#         reverse(l2)
#         print(l1)
#         print(l2)
           
#         i = 0
#         num = 1
#         for i in l1:
#             l1_new.append(i*num)
#             num = num * 10
            
#         i = 0
#         num = 1
#         for i in l2:
#             l2_new.append(i*num)
#             num = num * 10
            
#         l3_new = sum(l1_new) + sum(l2_new)
#         l3_new = str(l3_new)
#         l3_new = list(l3_new)
#         l3_new.reverse()
          
#         return l3_new