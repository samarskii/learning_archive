class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        good = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] == nums[j] and i < j:
                    good += 1

        return good
    
    
    
print(Solution().numIdenticalPairs([1,2,3,1,1,3]))

print(Solution().numIdenticalPairs([1,1,1,1]))

print(Solution().numIdenticalPairs([1,2,3]))