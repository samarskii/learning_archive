class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        x = list(x)
        check = list()
        for i in range(len(x)):
            if x[i-1] == x[-i]:
                check.append("Palindrome")
            else:
                check.append("Not palindrome")

        solution = None
        if "Not palindrome" in check:
            return False
        else: 
            return True
        
print(Solution().isPalindrome(121))