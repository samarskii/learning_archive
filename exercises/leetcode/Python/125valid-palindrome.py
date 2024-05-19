import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()      
        s = [i for i in s]
        print(s)

        
        for i in range(0, len(s)):
            if s[i] == s[-i-1]:
                continue
            else: 
                return False
            
        
        return True
        
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))

print(Solution().isPalindrome("race a car"))

print(Solution().isPalindrome(""))