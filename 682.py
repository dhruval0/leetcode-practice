class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        stack = []

        for i in operations:

            if i in ("C", "D", "+"):
                if i == "C":
                    stack.pop()
                
                elif i == "D":
                    double_score = stack[-1] * 2
                    stack.append(double_score)
                
                elif i == "+":

                    sum_of_num = stack[-1] + stack[-2]
                    stack.append(sum_of_num)

            else:
                stack.append(int(i))

        return sum(stack)

s_obj = Solution()

user_input = ["5","-2","4","C","D","9","+","+"]
output_of_it = s_obj.calPoints(user_input)

print(output_of_it)