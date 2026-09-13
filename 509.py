class Solution:
    def fib(self, n: int) -> int:
        mapping = {
            0 : 0,
            1 : 1,
        }

        def f(n):

            if n in mapping:
                return mapping.get(n)

            fibonaci_seq_sum = f(n-1) + f(n-2)
            mapping[n] = fibonaci_seq_sum

            return fibonaci_seq_sum

        return f(n)

s_obj = Solution()

user_input = 4
output_of_it = s_obj.fib(user_input)

print(output_of_it)