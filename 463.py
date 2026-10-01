class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()
        self.perimeter = 0
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for row in range(self.rows):
            for column in range(self.cols):
                if grid[row][column] == 1:
                    self.dfs(row, column)
                    return self.perimeter

        return 0

    def dfs(self, row: int, column: int) -> None:
        stack = [(row, column)]

        while stack:
            row, column = stack.pop()
            if (row, column) in self.visited:
                continue

            self.visited.add((row, column))

            for dr, dc in self.directions:
                next_row, next_col = row + dr, column + dc

                if not (0 <= next_row < self.rows and 0 <= next_col < self.cols):
                    self.perimeter += 1
                elif self.grid[next_row][next_col] == 0:
                    self.perimeter += 1
                elif (next_row, next_col) not in self.visited:
                    stack.append((next_row, next_col))

s_obj = Solution()

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

output_of_it = s_obj.islandPerimeter(grid)

print(output_of_it)