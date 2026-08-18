class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        stacks = []
        stackt = []

        for char in s:

            if char == "#":
                if stacks:
                    stacks.pop()
            else:
                stacks.append(char)
        
        for char in t:

            if char == "#":
                if stackt:
                    stackt.pop()
            else:
                stackt.append(char)
        
        if "".join(stacks) == "".join(stackt):
            return True

        return False

s_obj = Solution()

user_input = "ab#c"
user_second_input = "ad#c"
output_of_it = s_obj.backspaceCompare(user_input, user_second_input)

print(output_of_it)