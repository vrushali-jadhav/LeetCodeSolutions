class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        while i <= (len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)]==needle:
                return i
            i = i+1
        return -1

s = Solution()
x = s.strStr("hello","ll")
print(x)