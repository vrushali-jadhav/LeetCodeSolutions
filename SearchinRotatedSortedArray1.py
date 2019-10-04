#This solution is obviously not the best or even average solution. 
#As the fact that the array IS sorted (we just don't know from which point) is not getting utilised here
#Come up with a better solution babe. You can do it!
class Solution():
    def search(self, nums, target):
        i, j = 0, len(nums)//2
        if not nums:
            return -1
        if nums[0] == target:
            return 0
        while i<=(len(nums)//2)-1 and j<= len(nums)-1:
            if nums[i] == target:
                return i
            elif nums[j] == target:
                return j
            i+=1
            j+=1
        #there could be a j or i left that didn't get traversed because of "and" in condition above
        if j<= len(nums)-1 and nums[j]==target:
            return j
        elif i<=(len(nums)//2)-1 and nums[i]==target:
            return i
        return -1
s = Solution()
#print(s.search([4,5,6,7,0,1,2],0))
print(s.search([1],1))
print(s.search([1,3,5],5))