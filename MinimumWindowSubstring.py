import collections
class Solution(object):
    def minWindow(self, S, T):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #to reduce the counts if char is found
        count1={} 
        #to keep matching if the char is in the dict
        count2={}
        
        count1 = dict(collections.Counter(T))
        count2 = dict(collections.Counter(T))

        #keep decreasing the count. if all elements from right string are found, count would be 0
        count=len(T)
        start, minSize, minStart = 0, float("inf"), 0
        
        for indx, val in enumerate((S)):
        
            if val in count2 and count2[val]>0:
                #this will also set values to <0 when you encounter the char again 
                count1[val]-=1
                
                #found the element, so decrease the count
                if count1[val]>=0:
                    count-=1
            
            #the first time reach here, all the values in count are set to 0
            #indx is at the point where we found the last charchter we need
            #now we have to see if the can find the chars again
            if count==0:
                while True:
                    if S[start] in count2:
                        if count1[S[start]]<0:
                            count1[S[start]]+=1
                        else:
                            break
                    start+=1
                if minSize>indx-start+1:
                    minSize=indx-start+1 
                    minStart=start
        
        if minSize==float("inf"): 
            return ''
        else:
            return S[minStart:minStart+minSize]
        
s = Solution()

print(s.minWindow("ADOBECODEBANC","ABC"))