class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        current_sum = sum(nums[:k])
        max_sum = current_sum
        remove_index = 0

        for i in range(k, len(nums)):

            current_sum = current_sum - nums[remove_index] + nums[i]

            max_sum = max(max_sum, current_sum)

            remove_index += 1 

        return max_sum / k
                
s_obj = Solution()
user_input = [1,12,-5,-6,50,3]
output_of_it = s_obj.findMaxAverage(user_input, 4)

print(output_of_it)