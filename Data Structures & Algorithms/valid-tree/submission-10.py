class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        cycle = set()
        visit = set()
        adjList = {}
        for point in range(n):
            adjList[point] = []

        for e1, e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)
        
        def dfs(point, prev):
            if point in cycle:
                return False
            
            cycle.add(point)

            for p2 in adjList[point]:
                if p2 == prev:
                    continue
                
                if (dfs(p2, point) == False):
                    return False
            
            visit.add(point)
            cycle.remove(point)
            return True
        
        return dfs(0, -1) == True and len(visit) == n
        # if (len(visit) == n - 1 and dfs(0, -1) == True):
        #     return True
        # print(visit)

        # return False
