from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        
        current_sum = 0
        max_sum = nums[0]
        
        for x in nums:
            
            # Here i am checking the current subaaray sum is greater than current value or an element
            current_sum = max(current_sum + x, x)
            max_sum = max(max_sum, current_sum)

        return max_sum


s_obj = Solution()

user_input =[5,4,-1,7,8]
output_of_it = s_obj.maxSubArray(user_input)

print(output_of_it)