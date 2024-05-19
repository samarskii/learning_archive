class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        prefix = ""
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix += chars[0]
            else:
                break

        return prefix
        
        
        
        
        
print(Solution().longestCommonPrefix(["flower","flow","flight"]))

print(Solution().longestCommonPrefix(["dog","racecar","car"]))

print(Solution().longestCommonPrefix(["ab","a"]))


# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if len(strs) == 1:
#             return strs[0]
        
#         prefix = "list()"
#         for i in range(0, len(strs)):
#             for k in range(0, len([k for k in strs])):
#                 try:
#                     if len(strs) == 2:
#                         if strs[i][k] == strs[i+1][k]:
#                             prefix.append(strs[i][k])
#                     if strs[i][k] == strs[i+1][k] and strs[i+1][k] == strs[i+2][k]:
#                         prefix.append(strs[i][k])
#                 except:
#                     continue        
                
            
#         prefix = ''.join([str(elem) for elem in prefix])
        
#         return prefix