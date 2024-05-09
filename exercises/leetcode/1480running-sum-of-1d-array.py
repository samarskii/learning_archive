# class Solution(object):
#     def runningSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         new_num = list()
#         num = 0
#         for i in nums:
#             new_num.append(i+num)
#             num = i + num

#         return new_num


# Another aproach with rewriting original array

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if i == 0:
                nums[i] = nums[i]
            else:
                nums[i] = nums[i-1] + nums[i]
        return nums
    
print(Solution().runningSum([1,2,3,4]))