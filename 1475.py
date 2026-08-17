class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """

        stack = []
        answers = prices[:]

        for i in range(len(prices)):

            while stack and prices[i] <= prices[stack[-1]]:

                discounted_price = prices[stack[-1]] - prices[i]
                answers[stack[-1]] = discounted_price
                stack.pop()

            stack.append(i)

        return answers

s_obj = Solution()

user_input = [10,1,1,6]
output_of_it = s_obj.finalPrices(user_input)

print(output_of_it)