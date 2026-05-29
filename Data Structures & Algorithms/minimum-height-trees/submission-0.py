class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
            
        adjList = {}
        for i in range(n):
            adjList[i] = set()

        for p1, p2 in edges:
            adjList[p1].add(p2)
            adjList[p2].add(p1)

        leaves = [i for i in range(n) if len(adjList[i]) == 1]
        
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = adjList[leaf].pop()
                adjList[neighbor].remove(leaf)
                if len(adjList[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
            
        return leaves