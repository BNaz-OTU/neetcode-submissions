class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        neighbour = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))
                    visit.add((row, col))
        
        step = 0
        while len(queue) > 0:

            for _ in range(len(queue)):
                c_row, c_col = queue.popleft()
                grid[c_row][c_col] = step

                for dr, dc in neighbour:
                    n_row = c_row + dr
                    n_col = c_col + dc

                    if n_row < 0 or n_row >= ROWS or n_col < 0 or n_col >= COLS or grid[n_row][n_col] == -1 or (n_row, n_col) in visit:
                        continue
                    
                    queue.append((n_row, n_col))
                    visit.add((n_row, n_col))
            
            step += 1
        
