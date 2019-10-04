class Solution():
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] == 0:
                nums.pop(i) #do not increment i as you are removing i from this index
                nums.append(0)
                j -= 1 #reduce j as you have appended an extra 0 to the end
            else:
                i += 1
                
        return nums

s = Solution()
print(s.moveZeroes([0,0,0,0,3,12])) #[3,12,0,0,0,0]
print(s.moveZeroes([3,0,5])) #[4,2,4,3,5,1,0,0,0,0]