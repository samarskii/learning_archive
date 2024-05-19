class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        return sum(sum(int(digit) for digit in str(i)) % 2 == 0 for i in range(1, num + 1))
        
        
print(Solution().countEven(4)) # 2


print(Solution().countEven(30)) # 14
