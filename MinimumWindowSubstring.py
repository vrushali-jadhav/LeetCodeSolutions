import collections
class Solution(object):
    def minWindow(self, S, T):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dictForCount={} 
        dictForCount = dict(collections.Counter(T))
        
        count=len(T)
        start, minSize, minStart = 0, float("inf"), 0
        
        for indx, val in enumerate((S)):
            if val in dictForCount:
                dictForCount[val]-=1
                
                #-ve value would mean you are encountering the char 2nd time
                if dictForCount[val]>=0:
                    count-=1
            if count==0:
                while True:
                    if S[start] in dictForCount:
                        #this will only be negative if you encounter the char more than once
                        #now we have to check if the could be shorter
                        if dictForCount[S[start]]<0:
                            dictForCount[S[start]]+=1
                        else:
                            break
                    
                    #at first, start if pointing to the 1st char in dict when we have found all the expected chars
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

print(s.minWindow("dacab","ab"))
