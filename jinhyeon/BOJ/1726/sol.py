from collections import deque
m, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]
visited = [[[0] * n for _ in range(m)] for _ in range(4)]   # 바라보는 방향이 4방향이기 때문에

# print(visited)

start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))
dire = [(0, 1), (0, -1), (1, 0), (-1, 0)] #1 동, 2 서, 3 남, 4 북
dire_ban = [1, 0, 3, 2]   # 못가는 방향 인덱스

def bfs(d, x, y):   #d-1을 하고 온다
    q = deque()
    q.append((d, x, y))
    visited[d][x][y] = 1
    while q:
        d, x, y = q.popleft()
        if (x + 1, y + 1, d + 1) == end:
            return visited[d][x][y] - 1
        for i in range(1, 4): #방향에 따라 1칸에서 3칸
            nx, ny = x + dire[d][0] * i, y + dire[d][1] * i
            if not (0 <= nx < m and 0 <= ny < n) or arr[nx][ny]:
                break
            if visited[d][nx][ny]:
                continue
            q.append((d, nx, ny))
            visited[d][nx][ny] = visited[d][x][y] + 1
        for i in range(4):
            if i not in [d, dire_ban[d]]:
                if not visited[i][x][y]:
                    q.append((i, x, y))
                    visited[i][x][y] = visited[d][x][y] + 1
    return 0
ans = bfs(start[2]-1, start[0]-1, start[1]-1)
print(ans)