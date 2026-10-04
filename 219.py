class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()

        for i, num in enumerate(nums):

            if num in window:
                return True

            window.add(num)

            if len(window) > k:
                window.remove(nums[i - k])

        return False

s_obj = Solution()

nums = [1,2,3,1]
k = 3
output_of_it = s_obj.containsNearbyDuplicate(nums, k)

print(output_of_it)