class Solution:
    def isValid(self, inputString):
        """
        :type s: str
        :rtype: bool
        """    
        stack = []
        lookup = {"(":")","{":"}","[":"]"}

        for char in inputString:
            
            if char in lookup:
                stack.append(char)

            elif len(stack)==0 or char != lookup[stack.pop()]:
                return False
            
        return len(stack)==0

s = Solution()
print(s.isValid("([])"))
