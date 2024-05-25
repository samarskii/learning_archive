class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        
        for i in range(0, n):
            if 2 ** i == n:
                return True
            
        return False
            

print(Solution().isPowerOfTwo(1))

print(Solution().isPowerOfTwo(16))

print(Solution().isPowerOfTwo(3))


print(Solution().isPowerOfTwo(6))


# print(f"16 ** 1/2 {16 ** 0.5}")
# print(f"round(16 ** 1/2) {round(16 ** 0.5)}")