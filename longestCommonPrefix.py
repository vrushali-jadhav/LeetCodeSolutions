class Solution():
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        matchingLength = []
        if strs:
            if len(strs) == 1:
                return strs[0]                  
        else: 
            return ""
        
        for str1 in strs[1:]:
            index = 0
            while index < len(strs[0]) and index < len(str1):
                if strs[0][index] != str1[index]:
                    break
                index = index+1
            matchingLength.append(index)

        if matchingLength:        
            return strs[0][0:min(matchingLength)]
        else:
            return ""

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flor"]))

