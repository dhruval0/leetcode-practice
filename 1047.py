class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)

s_obj = Solution()

user_input = "abbaca"
output_of_it = s_obj.removeDuplicates(user_input)

print(output_of_it)