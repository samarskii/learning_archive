class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        last_letter = ""
        max_counter = 1
        counter = 1
        for i in s:
            if i == last_letter:
                counter += 1
                
                if i == last_letter and counter >= max_counter:
                    max_counter = counter

                last_letter = i
            else:
                last_letter = i
                counter = 1
            
        return max_counter
        
        
print(Solution().maxPower("leetcode"))


print(Solution().maxPower("abbcccddddeeeeedcba"))