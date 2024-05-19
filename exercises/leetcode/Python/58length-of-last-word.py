class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_list = s.split()
        
        return len(new_list[-1])
                
print(Solution().lengthOfLastWord("Hello World"))

print(Solution().lengthOfLastWord("   fly me   to   the moon  "))

print(Solution().lengthOfLastWord("luffy is still joyboy"))
