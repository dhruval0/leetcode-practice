class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """


        stack = []
        closing_opening_info = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        for i in s:
            
            if i in ["[", "(", "{"]:
                stack.append(i)
            
            elif i in ["]", "}", ")"]:

                top_of_stack = len(stack) - 1
                if len(stack) == 0:
                    return False

                elif i != closing_opening_info.get(stack[top_of_stack]):
                    return False

                del stack[top_of_stack]

        if len(stack) > 0:
            return False

        return True


s_obj = Solution()

user_input = "([])"
output_of_it = s_obj.isValid(user_input)

print(output_of_it)
