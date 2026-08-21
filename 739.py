class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        stack = []
        results = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[i] > stack[-1][0]:
                
                days_to_wait = i - stack[-1][1]

                temperatures_with_index = stack.pop()

                results[temperatures_with_index[1]] = (days_to_wait) 

            stack.append((temperatures[i], i))

        return results

s_obj = Solution()

user_input = [30,60,90]
output_of_it = s_obj.dailyTemperatures(user_input)

print(output_of_it)