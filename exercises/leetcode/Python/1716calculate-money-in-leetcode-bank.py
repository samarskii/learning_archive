class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        monday_counter = 0
        total_money = 0
        days_counter = 1
        
        for i in range(1, n + 1):
            if i > 7 and (i - 8) % 7 == 0:
                monday_counter += 1
                days_counter = 1 + monday_counter
                
            total_money += days_counter
            days_counter += 1

        return total_money
        
        
print(Solution().totalMoney(5))
print("\n\n")

print(Solution().totalMoney(10))
print("\n\n")

print(Solution().totalMoney(20))
print("\n\n")