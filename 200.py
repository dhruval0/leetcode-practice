from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        def dfs(row: int, col: int) -> None:
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or grid[row][col] != "1"
            ):
                return

            grid[row][col] = "0"

            dfs(row - 1, col)  # Up
            dfs(row + 1, col)  # Down
            dfs(row, col - 1)  # Left
            dfs(row, col + 1)  # Right

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    island_count += 1
                    dfs(row, col)

        return island_count

s_obj = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

output_of_it = s_obj.numIslands(grid)

print(output_of_it)