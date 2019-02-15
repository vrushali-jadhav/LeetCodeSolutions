class Solution():
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        #36ms.. 80% faster
        """ if str == '-' or str == '+':
            return 0
        str = str.strip()
        integer = []
        for index, char in enumerate(str):
            if char.isdigit() or (char == '-' and not integer) or (char == '+' and not integer):
                if (char == '+' and str[index+1] == '-') or (char == '-' and str[index+1] == '+'):
                    return 0 
                integer.append(char)
            elif integer and (''.join(integer) != '-') and (''.joing(integer)!= '+'):
                break
            else:
                return 0
        resultInt = int(''.join(integer)) if integer else 0
        if resultInt > 2147483647:
            return 2147483647
        elif resultInt < -2147483648:
            return -2147483648
        return resultInt """

        #32 ms.. 100% faster
        if str == '-' or str == '+':
            return 0
        str = str.strip()
        integer = []
        for index, char in enumerate(str):
                if char.isdigit():
                    integer.append(char)
                
                #append to the list if 1st charachter 
                elif char == '-':
                    if not integer:
                        integer.append(char)
                    #occurance of - after a digit or second occurance of -
                    else:
                        break
                    
                elif char == '+':
                    if not integer:
                        integer.append(char)
                    else:
                        break

                #if the list is empty still, return 0
                elif not integer:
                    return 0
                
                #if the list isn't empty and a charachter such as . (3.14) has come
                else: 
                    break
                        
        if ''.join(integer) == '-' or ''.join(integer) == '+':
            return 0

        resultInt = int(''.join(integer)) if integer else 0
        if resultInt > 2147483647:
            return 2147483647
        elif resultInt < -2147483648:
            return -2147483648
        return resultInt

s = Solution()
print(s.myAtoi("-3.14"))