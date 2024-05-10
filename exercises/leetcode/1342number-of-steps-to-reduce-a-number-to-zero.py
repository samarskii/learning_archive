# class Solution(object):
#     def numberOfSteps(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         counts = 0
#         while True:
#             if num == 0:
#                 False
#                 break
#             elif num % 2 == 0:
#                 num = num / 2
#                 counts += 1
#                 continue
#             elif num % 2 != 0:
#                 num = num - 1
#                 counts += 1
#                 continue

#         return counts


class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        counts = 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
                continue
            else:
                num == num - 1
                continue
            
            
            counts += 1

        return counts
        
        
print(Solution().numberOfSteps(14))

print(Solution().numberOfSteps(8))

print(Solution().numberOfSteps(123))