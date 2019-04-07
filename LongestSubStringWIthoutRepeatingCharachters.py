class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ocur = {}
        start = 0
        maxlength = 0
       
        for i, char in enumerate(s):
            if char in ocur and ocur[char]>=start:
                while(s[start] != char):
                    start += 1
                start +=1
            
            ocur[char] = i
            maxlength = max(maxlength, i-start+1)
        
        return maxlength

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))