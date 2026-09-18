class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:

        self.graph = {}
        self.visited = set()
        self.destination = destination

        for edge in edges:

            if edge[0] not in self.graph:
                self.graph[edge[0]] = [edge[1]]
            else:
                self.graph[edge[0]].append(edge[1])

            if edge[1] not in self.graph:
                self.graph[edge[1]] = [edge[0]]
            else:
                self.graph[edge[1]].append(edge[0])

        if source == destination:
            return True

        return self.dfs(source)

    def dfs(self, vertex):

        if vertex not in self.graph:
            return False

        if vertex not in self.visited:

            edges = self.graph.get(vertex)
            if self.destination in edges:
                return True

            self.visited.add(vertex)

            for edge in edges:
                if self.dfs(edge):
                    return True

        return False


s_obj = Solution()
n = 3
edges = [[0,1],[1,2],[2,0]]
# edges = [
#     [0, 1],
#     [0, 2],
#     [1, 3],
#     [2, 4]
# ]
source = 0
destination = 2

output_of_it = s_obj.validPath(n, edges, source, destination)

print(output_of_it)