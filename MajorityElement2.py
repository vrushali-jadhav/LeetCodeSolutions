import collections
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majorityNum = len(nums)/2        
        frequncy = {}
        
        for num in nums:
            if num not in frequncy:
                frequncy[num] = 1
            elif frequncy[num]+1>majorityNum:
                return num
            else:
                frequncy[num] += 1
        
        #if there's only 1 element in the list (since it went to 1st if)
        return nums[0]

s = Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))