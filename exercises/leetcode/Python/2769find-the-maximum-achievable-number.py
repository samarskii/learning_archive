class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        
        return num + t + t
        
        
print(Solution().theMaximumAchievableX(4, 1)) # must be 6

print(Solution().theMaximumAchievableX(3, 2)) # must be 7



# class Solution(object):
#     def theMaximumAchievableX(self, num, t):
#         """
#         :type num: int
#         :type t: int
#         :rtype: int
#         """
        
#         for i in range(t):
#             num = num + 2
            
#         return num