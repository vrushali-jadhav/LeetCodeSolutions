class Solution():
    dictStore = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    def romanToInt(self, s):
        intVal = 0
        index = 0
        while index <= len(s)-1:
            if index+1 <= len(s)-1:
                if self.dictStore[s[index]] < self.dictStore[s[index+1]]:
                    intVal = intVal+self.dictStore[s[index+1]]-self.dictStore[s[index]]
                    index += 2
                    continue
            intVal += self.dictStore[s[index]]
            index += 1
        return intVal

s = Solution()
print(s.romanToInt("IX"))