# class Solution(object):
#     def fizzBuzz(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """

#         answer = list()
        
#         for i in range(n+1):
#             if i == 0:
#                 pass
#             elif i % 3 == 0 and i % 5 == 0: 
#                 answer.append('FizzBuzz')
#             elif i % 3 == 0:
#                 answer.append("Fizz")
#             elif i % 5 == 0:
#                 answer.append("Buzz")
#             else:
#                 answer.append(str(i))
        
#         return answer       


# class Solution(object):
#     def fizzBuzz(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         return ["FizzBuzz" if number % 3==0 and number % 5 ==0 else "Fizz" if number % 3 ==0 else "Buzz" if number % 5 ==0 else str(number) for number in range(1,n+1)]
    
print(Solution().fizzBuzz(15))     