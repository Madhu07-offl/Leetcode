class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = set()
        stack = [0]

        while stack:
            room = stack.pop()

            if room not in visited:
                visited.add(room)
                stack.extend(rooms[room])

        return len(visited) == len(rooms)