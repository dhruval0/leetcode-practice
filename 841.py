class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:

        self.visited_rooms = set()
        self.rooms = rooms

        self.visited_rooms.add(0)
        self.dfs(0)

        return len(self.visited_rooms) == len(rooms)

    def dfs(self, room):

        for key in self.rooms[room]:

            if key not in self.visited_rooms:
                self.visited_rooms.add(key)
                self.dfs(key)

s_obj = Solution()

user_input = [[1,3],[3,0,1],[2],[0]]
output_of_it = s_obj.canVisitAllRooms(user_input)

print(output_of_it)