class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        copy = int(x)
        rev = self.recursive(0,copy)
        if rev == x:
            return True

    def recursive(self,reverseNum,copy):
        if copy:
            reverseNum = reverseNum*10
            reverseNum = reverseNum+copy%10
            copy = copy//10

            self.recursive(reverseNum,copy)
        else:
            return reverseNum 

s = Solution()
print(s.isPalindrome(1331))