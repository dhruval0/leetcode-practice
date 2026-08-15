class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left_p = 0
        right_p = len(nums) - 1
        result = [0] * len(nums)
        fill_up_position_in_result = right_p

        while left_p <= right_p:
            
            square_of_left_p = nums[left_p] * nums[left_p]
            square_of_right_p = nums[right_p] * nums[right_p]

            if square_of_left_p > square_of_right_p:
                result[fill_up_position_in_result] = square_of_left_p
                left_p += 1
            
            elif square_of_left_p <= square_of_right_p:
                result[fill_up_position_in_result] = square_of_right_p
            
                right_p -= 1

            fill_up_position_in_result -= 1

        return result

s_obj = Solution()

user_input = [1, 2, 3]
output_of_it = s_obj.sortedSquares(user_input)

print(output_of_it)
