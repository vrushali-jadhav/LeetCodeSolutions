class Solution():
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        index = len(s)-1
        
        while index>=0:
            if s[index] == " ":
                if length:
                    break
            else:
                length += 1
            index -= 1
        return length 

s = Solution()
print(s.lengthOfLastWord("a"))