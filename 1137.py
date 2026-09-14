class Solution:
    def tribonacci(self, n: int) -> int:
        mapping = {
            0 : 0,
            1 : 1,
            2 : 1,
        }

        def t(n):

            if n in mapping:
                return mapping.get(n)

            tribonacci_seq_sum = t(n-1) + t(n-2) + t(n-3)
            mapping[n] = tribonacci_seq_sum

            return tribonacci_seq_sum

        return t(n)

s_obj = Solution()

user_input = 25
output_of_it = s_obj.tribonacci(user_input)

print(output_of_it)