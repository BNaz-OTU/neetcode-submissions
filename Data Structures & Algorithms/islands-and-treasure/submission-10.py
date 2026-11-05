class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        # INF = 2147483647

        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == 0):
                    queue.append((row, col))
                    visit.add((row, col))
        
        dist = 0
        while len(queue) > 0:
            search = len(queue)
            dist += 1
            for _ in range(search):
                x, y = queue.popleft()

                for dr, dc in neighbors:
                    new_x = x + dr
                    new_y = y + dc

                    if ((new_x >= 0 and new_x < ROWS) and
                        (new_y >= 0 and new_y < COLS) and
                        grid[new_x][new_y] == 2147483647):
                        grid[new_x][new_y] = dist
                        queue.append((new_x, new_y))
                        # visit.add((new_x, new_y))
        
        # return 


        