class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        stack = []
        next_greater = {}

        for num in nums2:

            while stack and num > stack[-1]:
                
                next_greater.update({stack[-1] : num})
                stack.pop()

            stack.append(num)

        ans = []
        for i in nums1:

            next_greater_of_i = next_greater.get(i)
            if next_greater_of_i:
                ans.append(next_greater_of_i)
            else:
                ans.append(-1)

        return ans

s_obj = Solution()

user_input = [2,4]
user_second_input = [1,2,3,4]
output_of_it = s_obj.nextGreaterElement(user_input, user_second_input)

print(output_of_it)