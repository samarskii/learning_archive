class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if s == '':
            return True
        if t == '':
            return False
        
        s = [i for i in s]
        t = [i for i in t]
        
        pos = 0
        
        for i in s:
            try:
                pos = t.index(i, pos) + 1
            except ValueError:
                return False            
            
        return True
        
        
        
print(Solution().isSubsequence("abc", 'ahbgdc'))

print(Solution().isSubsequence("acb", 'ahbgdc'))

print(Solution().isSubsequence("axc", 'ahbgdc'))

print(Solution().isSubsequence("aaaaaa", 'bbaaaa'))


# class Solution(object):
#     def isSubsequence(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
        
#         if s == '':
#             return True
#         if t == '':
#             return False
        
#         s = [i for i in s]
#         t = [i for i in t]
        
#         pos1 = s.index(s[0])
        
#         for i in s:
#             if i in t and t.index(i) >=  pos1:
#                 pos1 = t.index(i)
#                 continue
#             else: return False
            
            
#         return True