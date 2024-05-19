from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return Counter(nums).most_common(1)[0][0]
    
    
print(Solution().majorityElement([3,2,3]))

print(Solution().majorityElement([2,2,1,1,1,2,2]))


print(Solution().majorityElement([14, 1, 3,3, 3, 0, 15, 14, 14, 14, 2, 2, 1, 1, 2,3]))















# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        
#         new_dict = dict()
        
#         for i in nums:
#             new_dict[i] = new_dict.get(i, 0) + 1
            
#         biggest = [(v, k) for k, v in new_dict.items()]
        
#         biggest.sort()
        
#         return biggest[-1][1]
    
    
# print(Solution().majorityElement([3,2,3]))

# print(Solution().majorityElement([2,2,1,1,1,2,2]))


# print(Solution().majorityElement([14, 1, 3,3, 3, 0, 15, 14, 14, 14, 2, 2, 1, 1, 2,3]))

