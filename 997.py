class Solution:
    # def findJudge(self, n: int, trust: list[list[int]]) -> int:

    #     if n == 1 :
    #         return 1

    #     self.graph = {}

    #     for edge in trust:

    #         if edge[1] not in self.graph:
    #             self.graph[edge[1]] = [edge[0]]
    #         else:
    #             self.graph[edge[1]].append(edge[0])

    #     if len(self.graph) > 1:
    #         return -1

    #     judge = list(self.graph.keys())[0]
    #     persons_that_trust_judge = len(self.graph.get(judge))
    #     if persons_that_trust_judge != (n-1):
    #         return -1

    #     return judge

    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1:
            return 1

        for person in range(1, n + 1):
            incoming_trust = 0
            trusts_someone = False

            for a, b in trust:
                if a == person:
                    trusts_someone = True
                if b == person:
                    incoming_trust += 1

            if not trusts_someone and incoming_trust == n - 1:
                return person

        return -1



s_obj = Solution()
n = 3
trust = [[1,3],[2,3],[3,3]]

output_of_it = s_obj.findJudge(n, trust)

print(output_of_it)