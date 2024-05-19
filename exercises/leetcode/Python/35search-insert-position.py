class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
                
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            current = nums[mid]
            

            if current == target:
                return mid
            elif current < target:
                start = mid + 1
        
            else:
                end = mid - 1
        
        # print(f"Target is {target}. Mid is {mid}. Current is {current}. Start is {start}. End is {end}")
        
        return start
            
            
print(Solution().searchInsert([1,3,5,6], 5))

print(Solution().searchInsert([1,3,5,6], 2))    

print(Solution().searchInsert([1,3,5,6], 7))







        


































# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """

#         start = 0
#         end = len(nums) - 1
        
#         while start < end:
#             mid = (start + end) // 2
#             current = nums[mid]
            
#             if current == target:
#                 return mid
#             elif current > target:
#                 end = mid - 1
#             else:
#                 start = mid + 1
                
#         return None
    
# print(Solution().searchInsert([1,3,5,6], 5))
            