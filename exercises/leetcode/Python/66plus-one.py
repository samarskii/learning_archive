class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        digits[-1] += 1

        while 10 in digits:
            if digits[0] == 10:
                digits.insert(0, 1)
                digits[1] = 0
            if 10 in digits:
                position_of_10 = digits.index(10)
                digits[position_of_10] = 0
                digits[position_of_10 - 1] += 1
            if 10 not in digits:
                False
        return digits

    
print(Solution().plusOne([1,2,3]))

print(Solution().plusOne([4,3,2,1]))

print(Solution().plusOne([9, 9]))
