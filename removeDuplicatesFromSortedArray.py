class Solution(object):
    def removeDuplicates(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        #this approach saves a lot of space but not execution time
        """ i=0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
                i -= 1
            i += 1
        return len(nums) """

        n = len(arr)
        if n == 0 or n == 1: 
            return n 
  
        temp = list(range(n)) 
  
        # Start traversing elements 
        j = 0; 
        for i in range(0, n-1):  
            if arr[i] != arr[i+1]: 
                temp[j] = arr[i] 
                j += 1
  
        temp[j] = arr[n-1] 
        j += 1
     
        for i in range(0, j): 
            arr[i] = temp[i] 
        
        print(arr)
        return j 

s = Solution()
arr = [0,0,1,1,1,2,2,3,3,4]
s.removeDuplicates(arr)
print(arr)