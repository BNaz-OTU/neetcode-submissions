class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}
        visit = set()
        count = 0

        for num in range(n):
            adjList[num] = []
        
        for val1, val2 in edges:
            adjList[val1].append(val2)
            adjList[val2].append(val1)
        
        def dfs(curNum, prevNum):
            if curNum in visit:
                return 
            
            visit.add(curNum)

            for val in adjList[curNum]:
                if val == prevNum:
                    continue
                
                dfs(val, curNum)

        for num in range(n):
            if num in visit:
                continue
            
            dfs(num, -1)
            count += 1
            

        return count