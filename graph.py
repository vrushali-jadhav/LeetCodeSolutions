from collections import defaultdict
class Solution:
    def criticalConnections(self, n, connections):
        graph = defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
            
        dfn = [None for i in range(n)]
        low = [None for i in range(n)]
        dfn1 = defaultdict(int)
        low1 = defaultdict(int)
        print(dfn1, graph, low1)
        
        cur = list(graph.keys())[0]
        start = list(graph.keys())[0]
        res = []
        self.cur = list(graph.keys())[0]
       
        def dfs(node,parent):
            if node not in dfn1.keys():
                dfn1[node] = self.cur
                low1[node] = self.cur
                self.cur+=1
                for n in graph[node]:
                    if dfn1[n] is None:
                        dfs(n,node)
                    
                if parent is not None:
                    l = min([low1[i] for i in graph[node] if i!=parent]+[low1[node]])
                else:
                    l = min(low1[i] for i in graph[node]+[low1[node]])
                low1[node] = l
                
        dfs(list(graph.keys())[0],None)

        
        print(dfn1, graph, low1)
        for v in connections:
            if low1[v[0]]>dfn1[v[1]] or low1[v[1]]>dfn1[v[0]]:
                res.append(v)
        return res

s = Solution()
print(s.criticalConnections(4, [[9,1],[1,2],[2,9],[1,3]]))