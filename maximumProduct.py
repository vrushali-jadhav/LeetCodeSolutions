class Solution():
    def maximumProduct(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max = float("-inf")
        local_max = 1
        local_min = 1

        for x in nums:
            local_max = max(1, local_max)
            if x > 0:
                local_max, local_min = local_max * x, local_min * x
            else:
                local_max, local_min = local_min * x, local_max * x
            global_max = max(global_max, local_max)
        return global_max

s = Solution()
print(s.maximumProduct([3,-4,5,2,-2]))
