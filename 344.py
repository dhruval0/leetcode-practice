class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        left_p = 0
        right_p = len(s) - 1

        while left_p < right_p:

            left_value = s[left_p]
            right_value = s[right_p]

            s[left_p] = right_value
            s[right_p] =  left_value

            left_p += 1
            right_p -= 1

        print(s)

s_obj = Solution()
user_input = ["H","a","n","n","a","h"]
output_of_it = s_obj.reverseString(user_input)

print(output_of_it)