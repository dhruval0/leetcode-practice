class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        total_profit = 0
        yesterday = prices[0]

        for i in range(1,len(prices)):

            today = prices[i]
            if today > yesterday:

                today_profit = today - yesterday
                total_profit += today_profit

            yesterday = today

        return total_profit


s_obj = Solution()

user_input = [1, 5, 3, 2, 6]
output_of_it = s_obj.maxProfit(user_input)

print(output_of_it)