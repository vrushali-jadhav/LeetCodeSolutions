class Solution():
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strInt = str(x)
        stack = []
        sign = ""    
            
        for index, char in enumerate(strInt):
            if char == "-" and index ==0:
                strInt = strInt.replace(char,"")
                sign = "-"
            else:
                stack.insert(0,char)
        
        if sign:
            stack.insert(0,sign)
            
        strStack = ''.join(i for i in stack)
        
        if abs(int(strStack)) > 2**31 - 1:
            return 0
        else:
            return(int(strStack))

s = Solution()
print(s.reverse(1534236469))