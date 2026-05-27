class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order  = []
        adjList = {}
        cycle = set()
        visited = set()

        def dfs(crs):
            if (crs in cycle):
                return False
            if (crs in visited):
                return True
            
            cycle.add(crs)

            for new_crs in adjList[crs]:
                if (dfs(new_crs) == False):
                    return False
                
            cycle.remove(crs)
            visited.add(crs)
            order.append(crs)
            return True

        for crs in range(numCourses):
            adjList[crs] = []
        
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        for crs in range(numCourses):
            if (dfs(crs) == False):
                return []
            
        return order