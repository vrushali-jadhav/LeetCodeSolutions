class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        maxTotal = 0
        startIndex = 0 
        endIndex = 0

        for num in nums:
            total = max(total+num,total)
            
            if total > maxTotal:
                maxTotal = total

        return maxTotal

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))