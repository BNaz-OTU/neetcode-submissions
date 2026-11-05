class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}
        visit = set()
        for num in range(n):
            adjList[num] = []

        for e1, e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)
        
        print(adjList)

        def dfs(point, prev):
            if point in visit:
                return False
            
            visit.add(point)

            for p2 in adjList[point]:
                if prev == p2:
                    continue
                
                dfs(p2, point)
        
        count = 0
        for num in range(n):
            if num in visit:
                continue
                
            dfs(num, -1)
            count += 1
        
        return count
