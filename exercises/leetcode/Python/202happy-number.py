class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next(number):
            total_sum = 0
            while number > 0:
                digit = number % 10
                total_sum += digit * digit
                number //= 10
            return total_sum

        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1

# # Example usage:
# print(Solution().isHappy(19))  # Output: True
# print(Solution().isHappy(2))   # Output: False



# class Solution(object):
    
#     def isHappy(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
        
#         n = list(str(n))
#         iterations = 0
        
#         while n != ['1']:
            
#             current = list()
#             for i in n:
#                 current.append(int(i) ** 2)
#             n = list(str(sum(current)))
            
#             iterations += 1
#             if iterations == 100:
#                 return False
                
#         return True  
        
        
        
print(Solution().isHappy(19))

print(Solution().isHappy(2))