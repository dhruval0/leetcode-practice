class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while left <= right:

            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1

        return -1
        
s_obj = Solution()

user_input = [-1,0,3,5,9,12]

output_of_it = s_obj.search(user_input, 9)

print(output_of_it)