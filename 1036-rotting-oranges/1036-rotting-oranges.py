class Solution:
    def orangesRotting(self, grid):
        m1, n1 = len(grid), len(grid[0])
        visited_graph = grid
        q = collections.deque()
        countFreshOrange = 0
        for i in range(m1):
            for j in range(n1):
                if visited_graph[i][j] == 2:
                    q.append((i, j))
                if visited_graph[i][j] == 1:
                    countFreshOrange += 1
        if countFreshOrange == 0:
            return 0
        if not q:
            return -1
        
        minutes = -1
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while q:
            size = len(q)
            while size > 0:
                x, y = q.popleft()
                size -= 1
                for dx, dy in dirs:
                    i, j = x + dx, y + dy
                    if 0 <= i < m1 and 0 <= j < n1 and visited_graph[i][j] == 1:
                        visited_graph[i][j] = 2
                        countFreshOrange -= 1
                        q.append((i, j))
            minutes += 1
        
        if countFreshOrange == 0:
            return minutes
        return -1