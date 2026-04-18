class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        INF = 2147483647
        neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))
                    visit.add((row, col))
        
        dist = 0
        while len(queue) > 0:
            curr_q = len(queue)
            for _ in range(curr_q):
                c_row, c_col = queue.popleft()

                if grid[c_row][c_col] == INF:
                    grid[c_row][c_col] = dist

                for dr, dc in neighbours:
                    n_row = c_row + dr
                    n_col = c_col + dc

                    if n_row < 0 or n_row >= ROWS or n_col < 0 or n_col >= COLS or grid[n_row][n_col] != INF or (n_row, n_col) in visit:
                        continue
                    
                    # if grid[n_row][n_col] > dist:
                    queue.append((n_row, n_col))
                    visit.add((n_row, n_col))
            
            dist += 1
        