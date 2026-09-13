from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        memo = {}

        def solve(i):
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(solve(i + 1), solve(i + 2))

            return memo[i]

        return min(solve(0), solve(1))


s_obj = Solution()

user_input = [10, 15, 20]
output_of_it = s_obj.minCostClimbingStairs(user_input)

print(output_of_it)