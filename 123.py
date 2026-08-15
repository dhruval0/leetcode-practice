class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_profit = 0
        if len(prices) > 1:

            left_bests = [0]
            lowest_price_in_left = prices[0]

            for i in range(1, len(prices)):

                todays_price = prices[i]
                
                if todays_price < lowest_price_in_left:
                    lowest_price_in_left = todays_price

                todays_profit = todays_price - lowest_price_in_left

                if todays_profit > left_bests[i - 1]:
                    left_bests.append(todays_profit)
                else:
                    left_bests.append(left_bests[i - 1])

            right_bests = [0] * len(prices)
            highest_price_in_right = prices[len(prices)-1]

            for i in range(len(prices) - 2, -1,  -1):
                
                todays_price = prices[i]

                if todays_price > highest_price_in_right:
                    highest_price_in_right = todays_price

                todays_profit = highest_price_in_right - todays_price

                if todays_profit > right_bests[i + 1]:
                    right_bests[i] = todays_profit
                else:
                    right_bests[i] = right_bests[i + 1]
            
            max_profit = right_bests[0]

            for i in range(len(prices)-1):

                profit_in_split = left_bests[i] + right_bests[i + 1]

                if profit_in_split > max_profit:
                    max_profit = profit_in_split

        return max_profit


s_obj = Solution()

user_input = [3, 3, 5, 0, 0, 3, 1, 4]
output_of_it = s_obj.maxProfit(user_input)

print(output_of_it)