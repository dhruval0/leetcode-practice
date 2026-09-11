from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        unique_val = set()

        for num in nums:

            if num in unique_val:
                return True

            unique_val.add(num)
        
        return False


s_obj = Solution()

user_input = [1,2,3,1]
output_of_it = s_obj.containsDuplicate(user_input)

print(output_of_it)