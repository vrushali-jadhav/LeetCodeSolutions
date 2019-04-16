import collections
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = sorted(collections.Counter(nums).items(), key = lambda t:t[1])
        tuple1 = dict1[0]
        return tuple1[0]
        
s = Solution()
print(s.singleNumber([1,1,2,2,1]))