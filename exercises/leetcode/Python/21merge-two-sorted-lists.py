class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return dummy.next


def arrayToList(array):
    if not array:
        return None
    head = ListNode(array[0])
    current = head
    for value in array[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def printList(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(values)

# Example 1
list1 = arrayToList([1, 2, 4])
list2 = arrayToList([1, 3, 4])
merged_list = Solution().mergeTwoLists(list1, list2)
printList(merged_list)  # Output: [1, 1, 2, 3, 4, 4]
        

