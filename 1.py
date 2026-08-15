class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}
        
        for i in range(len(nums)):
            
            needed_elemt = target - nums[i]

            if needed_elemt not in seen:
                seen.update({nums[i] : i})

            elif needed_elemt in seen:
                return [seen.get(needed_elemt), i]

s_obj = Solution()

user_input = [2,7,11,15]
target = 9
output_of_it = s_obj.twoSum(user_input, target)

print(output_of_it)