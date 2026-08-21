class RecentCounter(object):

    def __init__(self):
        self.queue = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """

        self.queue.append(t)
        current_time_range = [t - 3000, t]

        while self.queue and not self.queue[0] >= current_time_range[0] and self.queue[0] <= current_time_range[1]:
            self.queue.pop(0)

        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
param_1 = obj.ping(1)
