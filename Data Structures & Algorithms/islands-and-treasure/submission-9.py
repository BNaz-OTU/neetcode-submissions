class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        treasure = deque()
        visit = set()
        neighbor = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == 0):
                    treasure.append((row, col))
                    visit.add((row, col))
        
        dist = 0
        while len(treasure) > 0:
            dist += 1
            for _ in range(len(treasure)):
                row, col = treasure.popleft()

                for dr, dc in neighbor:
                    n_row = row + dr
                    n_col = col + dc

                    if ((n_row < 0 or n_row >= ROWS) or
                        (n_col < 0 or n_col >= COLS) or
                        (grid[n_row][n_col] == -1) or
                        ((n_row, n_col) in visit)):
                        continue
                    
                    visit.add((n_row, n_col))
                    grid[n_row][n_col] = dist
                    treasure.append((n_row, n_col))
