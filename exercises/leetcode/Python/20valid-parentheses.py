class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return False

        brackets = '()[]{}'
        s = [i for i in s]
        
        pairs = []
        
        for i in range(0, len(s)):
            value = s.pop(0)
            pairs.append(value)
            # print(pairs[-1])
            # print(pairs)
            
            try:
                if pairs[-1] in brackets and brackets.index(pairs[-1]) - brackets.index(pairs[-2]) == 1:
                    # print("SUCCES")
                    pairs.pop(-1)
                    pairs.pop(-1)
                    # print(f"Pairs is {pairs} and len(pairs) is {len(pairs)}")
                    
                    # print('\n\n')
                    continue
            except IndexError:
                continue
            
            
        if len(pairs) == 0:
            return True
        else:
            return False
        
        
# print(Solution().isValid("()"))

# print(Solution().isValid("()[]{}"))

# print(Solution().isValid("(]"))

# print(Solution().isValid("{[]}"))

# print(Solution().isValid("([)]"))



# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         if s == '':
#             return False

#         brackets = '()[]{}'
#         s = [i for i in s]
#         s.sort()
        
#         while s:
#             try:
#                 pairs = [s.pop(0), s.pop(0)]

#                 if pairs[0] in brackets and brackets.index(pairs[1]) - brackets.index(pairs[0]) == 1:
#                     continue
#                 else:
#                     try:
#                         for i in range(0, s):
#                             if s[i] == s[-i]:
#                                 # print(f"S[i] is {s[i]} and s[-i] is {s[-i]}")
#                                 return True
#                     except:    
#                         return False
#             except:
#                 False
                
#         return True