class Solution:

    def climbStairs(self, n: int) -> int:

        mapping_with_steps = {
            1 : 1,
            2 : 2,
        }

        def ways(n):

            if n in mapping_with_steps:
                return mapping_with_steps.get(n)

            steps_needs = ways(n-1) + ways(n-2)
            mapping_with_steps[n] = steps_needs

            return steps_needs

        return ways(n)

s_obj = Solution()

user_input = 5
output_of_it = s_obj.climbStairs(user_input)

print(output_of_it)