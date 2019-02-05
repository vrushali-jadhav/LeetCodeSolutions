class Solution():
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        """ i =0
        while i <= len(nums)-1:
            if nums[i] == val:
                nums.pop(i)
                i = i-1
            i = i+1
        return len(nums) """

        #this solution will move the elements to be removed towards the end of the list
        #and you can just seperate the list from that index 

        i,last = 0, len(nums)-1
        while i <= last:
            if nums[i] == val:
                tmp = nums[last]
                nums[last]=nums[i]
                nums[i]=tmp
                last -=1
            else:
                i = i+1
        return last+1
s = Solution()
print(s.removeElement([1],1))
