import collections
import heapq

class Solution():
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #SOLUTION 1: FASTEST: 28ms
        countOfNums = {}

        for num in nums:
            if num not in countOfNums:
                countOfNums[num] = 1
            else:
                countOfNums[num] += 1
                
        count = sorted(countOfNums, key = countOfNums.get, reverse = True)
        return(count[:k])
        
        #SOLUTION 2: 52ms
        #without using sort function 
        """ countOfNums = {}
        frequencyBucket = [None for i in range(len(nums)+1)]
        results = []

        for num in nums:
            if num not in countOfNums:
                countOfNums[num] = 1
            else:
                countOfNums[num] += 1
        
        frequencyBucket[0] = 0
        for key, val in countOfNums.items():
            if not frequencyBucket[val]:
                frequencyBucket[val] = [key]
            else:
                frequencyBucket[val].append(key)
        #print(frequencyBucket)
        i = len(frequencyBucket)-1
        j = 0
        while i>=0 and j< k:
            if frequencyBucket[i]:
                results.extend(frequencyBucket[i])
                j = j+1
            i -= 1 

        return results[:k] """

        #SOLUTION 3: 40ms
        #Using heap DS
        """ countOfNums = {}
        results = []
        for num in nums:
            if num not in countOfNums:
                countOfNums[num] = 1
            else:
                countOfNums[num] += 1
        
        heap = [(value, key) for key,value in countOfNums.items()]
        
        largest = heapq.nlargest(k, heap) 

        for val in largest:
            results.append(val[1])

        return results """

s = Solution()
print(s.topKFrequent([4,1,-1,2,-1,2,3],2))
