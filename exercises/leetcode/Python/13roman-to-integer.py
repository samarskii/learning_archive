class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_list = list(s)
        new_roman_list = list()


        for i in range(len(roman_list)):
            if roman_list[i] == 'I':
                try:
                    if roman_list[i+1] == 'V':
                        new_roman_list.append(-1)
                    elif roman_list[i+1] == 'X':
                        new_roman_list.append(-1)
                    else: 
                        new_roman_list.append(1)
                except:
                        new_roman_list.append(1)
            if roman_list[i] == 'V':
                new_roman_list.append(5)
            if roman_list[i] == 'X':
                try:
                    if roman_list[i+1] == 'L':
                        new_roman_list.append(-10)
                    elif roman_list[i+1] == 'C':
                        new_roman_list.append(-10)
                    else: 
                        new_roman_list.append(10)
                except:
                        new_roman_list.append(10)
            if roman_list[i] == 'L':
                new_roman_list.append(50)
            if roman_list[i] == 'C':
                try:
                    if roman_list[i+1] == 'D':
                        new_roman_list.append(-100)
                    elif roman_list[i+1] == 'M':
                        new_roman_list.append(-100)
                    else: 
                        new_roman_list.append(100)
                except:
                    new_roman_list.append(100)
            if roman_list[i] == 'D':
                new_roman_list.append(500)
            if roman_list[i] == 'M':       
                new_roman_list.append(1000)


        new_roman_list = sum(new_roman_list)
        return new_roman_list
