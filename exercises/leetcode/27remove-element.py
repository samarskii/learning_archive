class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        while val in nums:
            nums.pop(nums.index(val))
        
        return len(nums)
        
        
print(Solution().removeElement(nums=[3,2,2,3], val=3))
            
print(Solution().removeElement(nums=[0,1,2,2,3,0,4,2], val=2))
