class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for value in tokens:

            if value in ("+", "*", "-", "/"):
                
                second_value_from_stack = stack.pop(-1)
                first_value_from_stack = stack.pop(-1)

                if value == "+":
                    result = first_value_from_stack + second_value_from_stack
                elif value == "-":
                    result = first_value_from_stack - second_value_from_stack
                elif value == "/":
                    result = int(first_value_from_stack / second_value_from_stack)
                elif value == "*":
                    result = first_value_from_stack * second_value_from_stack
                
                stack.append(result)
            else:
                stack.append(int(value))
        
        return int(stack.pop())

s_obj = Solution()

user_input = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
output_of_it = s_obj.evalRPN(user_input)

print(output_of_it)