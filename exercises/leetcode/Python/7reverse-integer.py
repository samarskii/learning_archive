class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        
        new_list = str(x)
        
        new_list = [x for x in new_list]
        
        new_list.reverse()
        
        non_zero_position = None
        for i in range(0, len(new_list)):
            if new_list[i] != '0':
                non_zero_position = i
                break
        
        if non_zero_position is None:
            return 0
        
        the_new_list = new_list[non_zero_position:]
        
        if the_new_list[-1] == '-':
            the_new_list.insert(0, '-')
            the_new_list.pop()   

        the_new_list = int(''.join(the_new_list))
        
        return sign * the_new_list

# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
        
#         new_list = str(x)
#         new_list = [x for x in new_list]
#         new_list.reverse()
        
#         last_zeroeth = list()
        
#         for i in range(0, len(new_list)):
#             if new_list[i] != '0':
#                 last_zeroeth.append(new_list[i])
                
#         non_zero_position = int(last_zeroeth[0])
        
#         next_non_zero_position = new_list.index(str(non_zero_position))     
        
#         the_new_list = new_list[next_non_zero_position:]
        
#         if the_new_list[-1] == '-':
#             the_new_list.insert(0, '-')
#             the_new_list.pop()   

#         the_new_list = int(''.join(the_new_list))
        
#         return the_new_list


        
        
# print(Solution().reverse(123))

        
print(Solution().reverse(-123))
        
print(Solution().reverse(102000))

print(Solution().reverse(1534236469))