import collections
class Solution(object):
    def minWindow(self, S, T):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #to reduce the counts if char is found
        dictForCount={} 
        dictForCount = dict(collections.Counter(T))
        
        #keep decreasing the count. if all elements from right string are found, count would be 0
        count=len(T)
        start, minSize, minStart = 0, float("inf"), 0
        
        for indx, val in enumerate((S)):
            if val in dictForCount:
                #this will also set values to <0 when you encounter the char again 
                dictForCount[val]-=1
                
                #found the element, so decrease the count
                if dictForCount[val]>=0:
                    count-=1
            
            #the first time reach here, all the values in count are set to 0
            #indx is at the point where we found the last charchter we need
            #now we have to see if the can find the chars again
            if count==0:
                while True:
                    if S[start] in dictForCount:
                        if dictForCount[S[start]]<0:
                            dictForCount[S[start]]+=1
                        else:
                            break
                    #increment start it points to a char that is in the dict
                    start+=1
                if minSize>indx-start+1:
                    minSize=indx-start+1 
                    minStart=start
        
        if minSize==float("inf"): 
            return ''
        else:
            return S[minStart:minStart+minSize]
        
s = Solution()

print(s.minWindow("dbcab","ab"))
