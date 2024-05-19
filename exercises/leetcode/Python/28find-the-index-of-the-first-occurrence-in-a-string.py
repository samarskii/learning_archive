class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        
        
print(Solution().strStr(haystack="sadbutsad", needle="sad"))

print(Solution().strStr(haystack="leetcode", needle="leeto"))