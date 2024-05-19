class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        
        first, second = 1, 1
        
        for i in range(2, n + 1):
            current = first + second
            first = second
            second = current
        
        return second

print(Solution().climbStairs(7))




# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         first, second, iteration, i = 1, 1, 0, 1

#         if n <= 1:
#             return 1
        
#         while i < n:
#             iteration = first + second
#             first, second = second, iteration
#             i += 1
        
#         return iteration
    
# print(Solution().climbStairs(7))