import collections
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majorityNum = len(nums)/2
        frequency = collections.Counter(nums)
        
        
        for key, val in frequency.items():
            if val > majorityNum:
                return key

s = Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))