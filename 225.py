class MyStack(object):

    def __init__(self):
        self.queue = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        self.queue.append(x)

        index_of_element_that_added = len(self.queue) - 1

        if index_of_element_that_added:
            for i in range(index_of_element_that_added):

                add_back_of_queue = self.queue.pop(0)
                self.queue.append(add_back_of_queue)

    def pop(self):
        """
        :rtype: int
        """

        return self.queue.pop(0)

    def top(self):
        """
        :rtype: int
        """
        
        if len(self.queue) >= 1:
            return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """

        if len(self.queue) != 0:
            return False

        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(1)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()