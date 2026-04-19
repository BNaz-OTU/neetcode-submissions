class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}
        visit = set()
        count = 0

        for num in range(n):
            adjList[num] = []
        
        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
        
        def dfs(curNum, preNum):
            if curNum in visit:
                return
            
            visit.add(curNum)

            for val in adjList[curNum]:
                if val == preNum:
                    continue
                
                dfs(val, curNum)
            return
        
        for num in range(n):
            if num in visit:
                continue
            
            dfs(num, -1)
            count += 1
        
        return count
        
