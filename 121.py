class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_profit = 0
        buy_price = prices[0]

        for current_price in prices:
            
            if current_price < buy_price:
                buy_price = current_price

            todays_profit = current_price - buy_price

            if todays_profit > max_profit:
                max_profit = todays_profit
        
        return max_profit

s_obj = Solution()

user_input = [7,6,4,3,1]
output_of_it = s_obj.maxProfit(user_input)

print(output_of_it)