class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}
        visit = set()

        for num in range(n):
            adjList[num] = []
        
        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
        
        def dfs(curNum, preNum):
            if curNum in visit:
                return False
            
            visit.add(curNum)

            for val in adjList[curNum]:
                if preNum == val:
                    continue
                
                if not dfs(val, curNum):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visit) == n
        # print(adjList)
        # return True