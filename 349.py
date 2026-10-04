class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))

s_obj = Solution()

nums1 = [1,2,2,1]
nums2 = [2,2]
output_of_it = s_obj.intersection(nums1, nums2)

print(output_of_it)