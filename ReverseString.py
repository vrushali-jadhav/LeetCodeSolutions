class Solution():
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while i< len(s)-1 and j>=i:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i +=1
            j -=1
        return s

s = Solution()
print(s.reverseString(["h","e","l","l","o"]))