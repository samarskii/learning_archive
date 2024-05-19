class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        initial = 0
        for i in operations:
            if i == '++X' or i == 'X++':
                initial += 1
            if i == '--X' or i == 'X--':
                initial -= 1
                
        return initial
    
print(Solution().finalValueAfterOperations(["++X","++X","X++"]))