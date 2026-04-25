class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}
        visit = set()
        counter = 0

        for num in range(n):
            adjList[num] = []
        
        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
        
        def dfs(node, prev):
            if node in visit:
                return
            
            visit.add(node)

            for val in adjList[node]:
                if val == prev:
                    continue

                dfs(val, node)
            
        for num in range(n):
            if num in visit:
                continue
            else:
                dfs(num, -1)
                counter += 1
        
        return counter
