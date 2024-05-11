class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum = int(a, 2) + int(b, 2)
        return bin(sum)[2:]
        
        
        
   
print(Solution().addBinary(a="11", b="1"))

print(Solution().addBinary(a="1010", b="1011"))
