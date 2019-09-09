class Solution:
    def isHappy(self, n: int) -> bool:
        dictOfSum = {}
        while(True):
            length = len(str(n))
            i = length
            sum = 0
            if length == 1:
                n = n**2
                sum = n
            else:
                while(i>1):
                    i-=1
                    sum += ((n%10)*(n%10))            
                    n = int(str(n)[:-1])
                sum +=  (n*n)  
            if(sum == 1):
                return True
            n = sum
            if(sum not in dictOfSum):
                dictOfSum[sum] = 1
            else:
                return False
s = Solution()
print(s.isHappy(19))
