class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        answer = []
        for i in range(0, len(nums)):
            nums_of_i = nums[i]
            ans_of_i = nums[nums_of_i]
            answer.append(ans_of_i)

        return answer

s_obj = Solution()

user_input = [5,0,1,2,3,4]

output_of_it = s_obj.buildArray(user_input)

print(output_of_it)
