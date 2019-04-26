class Solution():
    def maximumProduct(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max, local_max, local_min = float("-inf"), 1, 1
        for x in nums:
            local_max, local_min = max(x, local_max * x, local_min * x), min(x, local_max * x, local_min * x)
            global_max = max(global_max, local_max)
        return global_max

s = Solution()
print(s.maximumProduct([3,-4,5,2,-2]))
