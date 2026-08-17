class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        right_p = len(numbers) - 1
        left_p = 0

        while left_p < right_p:
            sum_of_numbers = numbers[left_p] + numbers[right_p]

            if sum_of_numbers == target:
                return [left_p + 1, right_p + 1]

            if sum_of_numbers > target:
                right_p -= 1
            else:
                left_p += 1
        # for i in range(len(numbers)):
        #     sum_of_numbers = numbers[left_p] + numbers[right_p]
        #     if sum_of_numbers == target:
        #         return [left_p + 1, right_p + 1]
        #     if sum_of_numbers > target:
        #         right_p -= 1
        #     else:
        #         left_p += 1

s_object = Solution()

user_input = [-1,0]
target = -1
output_of_it = s_object.twoSum(user_input, target)

print(output_of_it)