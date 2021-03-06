import collections
class Solution():
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        dict1 = {}
        for c in s:
            if c not in dict1:
                dict1[c] = 1
            else:
                dict1[c] += 1
        
        for char in t:
            if char in dict1:
                dict1[char]-=1
            else:
                return False
            
            if dict1[char] == 0:
                dict1.pop(char)
                
        if dict1:
            return False
        else:
            return True

s = Solution()
print(s.isAnagram("anagram","nagaram"))
