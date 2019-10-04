class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortedList = sorted(nums) #will be used for comparing the actual array
        #The length from the 1st index to the last index that don't match, need to replaced
        left, right = 0, len(nums)-1
        #A while loop of this sort is will give TC of (nlogn)
        #As you dont even enter the loop if niether first nor the last number match the sorted arrays first/last number
        while (sortedList[left] == nums[left]) or (sortedList[right] == nums[right]):  
            if right-left <=1 :
                return 0   
            #if its same, its at the correct place. Move on.
            if sortedList[left] == nums[left]:      
                left += 1
            if sortedList[right] == nums[right]:
                right -= 1
        return right-left+1
s = Solution()
print(s.findUnsortedSubarray([1,3,2,2,2]))
                            #[1,2,2,2,3]
print(s.findUnsortedSubarray([2,6,4,8,10,9,15]))
                            #[2,4,6,8,9,10,15]
print(s.findUnsortedSubarray([5,4,3,2,1]))
                            #[1,2,3,4,5]
print(s.findUnsortedSubarray([2,1]))
print(s.findUnsortedSubarray([1,2,6,5,4,9]))
print(s.findUnsortedSubarray([1,2,3,3,3]))
print(s.findUnsortedSubarray([1,3,2,3,3]))
print(s.findUnsortedSubarray([2,3,3,2,4]))
print(s.findUnsortedSubarray([1,2,3,4]))
