import collections
class Solution():
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        people = {}
        for trusterAndTrusted in trust:
            people[trusterAndTrusted[0]] = -1

            if trusterAndTrusted[1] not in people:
                people[trusterAndTrusted[1]] = 1
            elif people[trusterAndTrusted[1]] == -1:
                continue
            else:
                 people[trusterAndTrusted[1]] += 1

        for person, trustedcount in people.items():
            if trustedcount == N-1:
                return person
        
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