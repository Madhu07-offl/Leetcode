class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = set()
        provinces = 0

        for i in range(n):
            if i not in visited:
                provinces += 1
                stack = [i]

                while stack:
                    city = stack.pop()

                    if city not in visited:
                        visited.add(city)

                        for j in range(n):
                            if isConnected[city][j] == 1 and j not in visited:
                                stack.append(j)

        return provinces