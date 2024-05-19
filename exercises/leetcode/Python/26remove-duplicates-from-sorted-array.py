class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
                
        return l
        
        

        
        
print(Solution().removeDuplicates([1,1,2]))

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))



# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        
#         new_nums = list()
#         for i in nums:
#             if i not in new_nums:
#                 new_nums.append(i)
#         nums[:] = new_nums
        
#         return len(nums)