class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        self.visited_vertices = set()
        self.current_path = set()
        self.neighbors = {}

        for course, prerequisite in prerequisites:
            if prerequisite not in self.neighbors:
                self.neighbors[prerequisite] = [course]
            else:
                self.neighbors[prerequisite].append(course)

        for course in range(numCourses):
            if self.dfs(course):
                return False

        return True

    def dfs(self, course):

        if course in self.current_path:
            return True

        if course in self.visited_vertices:
            return False

        self.current_path.add(course)

        for neighbor in self.neighbors.get(course, []):
            if self.dfs(neighbor):
                return True

        self.current_path.remove(course)
        self.visited_vertices.add(course)


        return False


s_obj = Solution()

numCourses = 2
prerequisites = [[1, 0]]

output_of_it = s_obj.canFinish(numCourses, prerequisites)

print(output_of_it)