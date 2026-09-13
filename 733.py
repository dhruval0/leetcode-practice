from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        original_color = image[sr][sc]

        # If the colors are already the same, nothing to do
        if original_color == color:
            return image

        def dfs(r, c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return

            if image[r][c] != original_color:
                return

            image[r][c] = color

            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        dfs(sr, sc)

        return image


s_obj = Solution()

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
output_of_it = s_obj.floodFill(image, sr, sc, color)

print(output_of_it)