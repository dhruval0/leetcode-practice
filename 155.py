class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        
        if self.stack and self.stack[-1][1] < value:
            self.stack.append((value, self.stack[-1][1]))
        
        else:
            self.stack.append((value, value))

    def pop(self):
        """
        :rtype: None
        """

        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(4)
obj.push(5)
obj.push(3)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()