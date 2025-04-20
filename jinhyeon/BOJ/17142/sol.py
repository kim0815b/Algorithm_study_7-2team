from collections import deque
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

virus = []
empty = 0
dxl = [1, -1 , 0, 0]
dyl = [0, 0, 1, -1]
min_val = float('inf')
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            virus.append((i, j))
        if arr[i][j] == 0:
            empty += 1

def dfs(idx, path):
    global min_val
    if len(path) == m:
        min_val = min(min_val, bfs(path))
        return
    if m > len(path) + len(virus) - idx:    #앞으로 놓을 수 있는 칸에 모두 놓아도 m만큼 둘 수 없을 때
        return
    path.append(virus[idx])
    dfs(idx + 1, path)
    path.pop()
    dfs(idx + 1, path)

def bfs(path):
    visited = [[0] * n for _ in range(n)]
    for x, y in path:
        visited[x][y] = 1
    dq = deque()
    dq.extend(path[:])
    last_virus = empty
    last = 0
    if not last_virus:
        return 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in zip(dxl, dyl):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] != 1:
                if arr[nx][ny] == 0:
                    last_virus -= 1
                visited[nx][ny] = visited[x][y] + 1
                last = visited[x][y]
                dq.append((nx, ny))
                if min_val < last:  #최소 값보다 크면 가지치기
                    return min_val
                if last_virus == 0:
                    return last
    return min_val

dfs(0, [])
print(-1 if min_val == float('inf') else min_val)