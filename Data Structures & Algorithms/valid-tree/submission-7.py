class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}
        visit = set()

        for nums in range(n):
            adjList[nums] = []
        
        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
        
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)

            for value in adjList[node]:
                if prev == value:
                    continue
                
                if not dfs(value, node):
                    return False
            
            return True

        if dfs(0, -1) and len(visit) == n:
            return True
        
        return False
