class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        """ matrix = [[False for i in range(len(s))] for j in range(len(s))] 
        index = 0
        lengthOfSubstring = 1

        while lengthOfSubstring <= len(s):
            while index + lengthOfSubstring <= len(s):
                #print(s[index:index+lengthOfSubstring])
                #if there's a direct match for the string in the dictionary
                if s[index:index+lengthOfSubstring] in wordDict:
                    matrix[index][index+lengthOfSubstring-1] = True
                
                j=0
                while j+index+1<= lengthOfSubstring-1:
                    if matrix[index][j+index] and matrix[j+index+1][index+lengthOfSubstring-1]:
                        matrix[index][index+lengthOfSubstring-1] = True 
                    j += 1
                index += 1

            lengthOfSubstring += 1
            index = 0

        print(matrix)
        return matrix[0][len(s)-1] """
        n = len(s)

        max_len = 0
        for string in wordDict:
            max_len = max(max_len, len(string))

        can_break = [False for _ in range(n + 1)]
        can_break[0] = True
        for i in range(1, n + 1):
            for l in range(1, min(i, max_len) + 1):
                if can_break[i-l] and s[i-l:i] in wordDict:
                    can_break[i] = True
                    break

        return can_break[-1]


s = Solution()
#print(s.wordBreak("catand", ["cats", "dog", "sand", "and", "cat"]))
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
#print(s.wordBreak("bba", ["b", "a"]))
#print(s.wordBreak("cars", ["car", "ca", "rs"]))
