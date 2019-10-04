class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end, startFlag = 0, 0, 0
        sortedList = sorted(nums)

        for index in range(len(nums)):
            if nums[index] == sortedList[index]:
                continue
            else:
                if not startFlag:
                    startFlag = 1
                    start = index
                else:
                    end = index
        if end == start and end == 0:
            return 0
        return end-start+1

s = Solution()
print(s.findUnsortedSubarray([1,3,2,2,2]))
print(s.findUnsortedSubarray([2,6,4,8,10,9,15]))
print(s.findUnsortedSubarray([5,4,3,2,1]))
print(s.findUnsortedSubarray([2,1]))
print(s.findUnsortedSubarray([1,2,6,5,4,9]))
print(s.findUnsortedSubarray([1,2,3,3,3]))
print(s.findUnsortedSubarray([1,3,2,3,3]))
print(s.findUnsortedSubarray([2,3,3,2,4]))
