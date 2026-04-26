class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}
        visit = set()

        for num in range(n):
            adjList[num] = []
        
        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
        
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)

            for val in adjList[node]:
                if val == prev:
                    continue

                if not dfs(val, node):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n

