class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        result = len(nums)

        for i in range(len(nums)):
            result ^= i
            result ^= nums[i]

        return result

s_obj = Solution()

nums = [3,0,1]
output_of_it = s_obj.missingNumber(nums)

print(output_of_it)