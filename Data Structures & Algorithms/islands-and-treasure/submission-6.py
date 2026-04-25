class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))
                    visit.add((row, col))
        
        travel = 0
        while len(queue) > 0:
            for idx in range(len(queue)):
                row, col = queue.popleft()

                grid[row][col] = travel
                # visit.add((row, col))

                for dr, dc in neighbors:
                    n_row = row + dr
                    n_col = col + dc

                    if (n_row < 0 or n_row >= ROWS) or (n_col < 0 or n_col >= COLS) or ((n_row, n_col) in visit) or (grid[n_row][n_col] == -1):
                        continue
                    
                    queue.append((n_row, n_col))
                    visit.add((n_row, n_col))
            travel += 1

