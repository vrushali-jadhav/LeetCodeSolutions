class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if target-num in dic:
                return [dic[target-num],i]
            dic[num] = i

s = Solution()
print(s.twoSum([-1,-2,-3,-4,-5], -8))

