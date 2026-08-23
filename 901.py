class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """

        if not self.stack:
            self.stack.append((price, 1))
        
        else:
            
            span_of_price = 1
            while self.stack and self.stack[-1][0] <= price:

                span_of_price += self.stack[-1][1]
                self.stack.pop()

            self.stack.append((price, span_of_price))
        
        return self.stack[-1][1]

# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
param_1 = obj.next(100)
param_1 = obj.next(80)
param_1 = obj.next(60)
param_1 = obj.next(70)
param_1 = obj.next(60)
param_1 = obj.next(75)
param_1 = obj.next(85)

print(param_1)