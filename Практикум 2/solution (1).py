import numpy as np
from copy import deepcopy


class Surface:
    def __init__(self, faces):
        self.triangles = faces
        self.graph = self.get_graph()
        self.n = len(self.graph)

    def get_graph(self):
        v_size = max(map(max, self.triangles)) + 1
        graph = [[0 for x in range(v_size)] for y in range(v_size)]
        for triangle in self.triangles:
            for i in range(3):
                graph[triangle[i - 1]][triangle[i]] += 1
        return graph

    def is_surface(self):
        def form_cycle(vers):
            n = len(vers)
            used = [0] * (len(self.graph) + 1)
            visited = [0]
            found_cycle = [False]

            def dfs(prev, u):
                if found_cycle[0]:
                    return
                used[u] = 1
                visited[0] += 1
                if visited[0] == n + 1:
                    found_cycle[0] = True
                    return
                for v in vers:
                    if v == prev or self.graph[u][v] + self.graph[v][u] == 0:
                        continue
                    if visited[0] == n:
                        if v == vers[0]:
                            dfs(u, v)
                    elif used[v] == 0:
                        dfs(u, v)
                used[u] = 0
                visited[0] -= 1

            dfs(-1, vers[0])
            return found_cycle[0]

        for u in range(self.n):
            neighbors = []
            for v in range(self.n):
                if self.graph[u][v] or self.graph[v][u]:
                    neighbors.append(v)

            flag = form_cycle(neighbors)

            if not flag:
                return False

        for i in range(self.n):
            for j in range(self.n):
                if self.graph[i][j] + self.graph[j][i] != 0 and self.graph[i][j] + self.graph[j][i] != 2:
                    return False

        return True

    def is_connected(self):
        used = [0] * self.n

        def dfs(u):
            used[u] = 1
            for v in range(self.n):
                if (self.graph[u][v] or self.graph[v][u]) and not used[v]:
                    dfs(v)

        dfs(0)
        return sum(used) == self.n

    def is_oriented(self):
        for u in range(self.n):
            for v in range(u + 1, self.n):
                if self.graph[u][v] + self.graph[v][u] == 0:
                    continue
                if not self.graph[u][v] or not self.graph[v][u]:
                    return False
        return True

    def _is_oriented(self, graph):
        res = 1
        n = len(graph)
        for u in range(n):
            for v in range(u + 1, n):
                if graph[u][v] + graph[v][u] == 0:
                    continue
                if not graph[u][v] or not graph[v][u]:
                    res = 0
        return bool(res)

    def is_orientable(self):
        if self.is_oriented():
            return True
        graph = deepcopy(self.graph)
        triangles = deepcopy(self.triangles)

        def rec(i):
            if i == len(triangles):
                if self._is_oriented(graph):
                    return True, triangles
                return False, []
            result = rec(i + 1)
            if result[0]:
                return result
            triangle = triangles[i]
            a, b, c = triangle
            triangles[i] = (b, a, c)
            graph[a][b] -= 1
            graph[b][c] -= 1
            graph[c][a] -= 1
            graph[b][a] += 1
            graph[c][b] += 1
            graph[a][c] += 1
            result = rec(i + 1)
            if result[0]:
                return result
            return False, []

        result = rec(0)
        if not result[0]:
            return False
        return True

    def Euler(self):
        v_size = self.n
        e_size = 0
        f_size = len(self.triangles)
        for u in range(v_size):
            for v in range(u + 1, v_size):
                if self.graph[u][v] or self.graph[v][u]:
                    e_size += 1
        return v_size - e_size + f_size
