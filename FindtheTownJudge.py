import collections
class Solution():
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N==1:
            return 1
        
        #dictionary after processing all the input
        people = {}
        #potential judges
        potentialJudge = []

        for trusts in  trust:
            #since this person has trusted someone else, they can't be the judge
            people[trusts[0]] = -1
            if(trusts[0] in potentialJudge):
                potentialJudge.remove(trusts[0])
            
            #this is the first time we came across a person who's trusted by someone
            #add in to the dict of potential judges
            if trusts[1] not in people:
                #create a list of lenght equal to N
                peopleWhoTrust = [0] * N
                #set value as 1 for the person who trusts this potential judge
                peopleWhoTrust[trusts[0]-1] = 1
                people[trusts[1]] = peopleWhoTrust  
                #add them to potential judge list
                potentialJudge.append(trusts[1])
            else:
                #This person is already in the dictionary. Which could mean followings:
                #1] They has trusted someone (so not a judge)
                if people[trusts[1]] == -1:
                    # remove them from potential judge list if they are in it
                    if trusts[1] in potentialJudge:
                        potentialJudge.remove(trusts[1])
                    continue
                #2] They are trusted by new person and don't trust anyone. 
                else:
                    trustedBy = people[trusts[1]]
                    trustedBy[trusts[0]-1] = 1
                    people[trusts[1]] = trustedBy
                #print("People's dict after else is: {0}".format(people))
            #print("People's dict after every trust relation is: {0}".format(people))
        #print("potentialJudge's list after processing the input is: {0}".format(potentialJudge))
        # Use the potential judge list to find the judge
        #either the list is empty, or many people in the list
        if len(potentialJudge)!=1:
            return -1
        else:
            #the number of 1's in the list of the judges trusters should be N-1 (everyone trusts him except himself)
            trustersList = people[potentialJudge[0]]
            ctr = collections.Counter(trustersList)
            count = ctr[1]
            #print("Count is: {0}".format(count))
            if count == N-1:
                return potentialJudge[0]
            else:
                return -1

s = Solution()
print(s.findJudge(3, [[1,3],[2,3]]))
print(s.findJudge(4, [[1,2], [1,3], [1,4], [2,1], [2,3], [4,1], [4,3]]))
print(s.findJudge(3, [[1,2],[1,3],[2,1],[3,2]]))
print(s.findJudge(5, [[1,2],[1,3],[1,5],[2,3],[2,4],[5,3]]))

'''
{
    1: -1,
    2: -1,
    3: [1,1,0]
}
potentialJudge = [3]
judge: 3

{
    1: -1,
    2: -1,
    3: [1,1,0,1],
    4: -1
}
potentialJudge = [3]
judge: 3

{
    1: -1,
    2: -1,
    3: -1
}
potentialJudge: []
judge: -1

{
    1: -1,
    2: -1,
    3: [1,1,0,0,1],
    4: [0,1,0,0,0],
    5: -1
}
potentialJudge: [3,4]
judge: -1
'''