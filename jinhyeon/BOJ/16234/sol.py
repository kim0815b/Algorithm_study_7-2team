from collections import deque
n, l, r = map(int, input().split())
dxl = [1, -1, 0, 0]
dyl = [0, 0, 1, -1]
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
def bfs(i, j):
    bfs_q = deque()
    q = deque()
    bfs_q.append((i, j))
    q.append((i, j))

    visited[i][j] = 1
    total = arr[i][j]

    flag = False
    while bfs_q:
        x, y = bfs_q.popleft()
        for dx, dy in zip(dxl, dyl):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n \
                    and not visited[nx][ny] and l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                flag = True
                bfs_q.append((nx, ny))
                q.append((nx, ny))
                total += arr[nx][ny]
                visited[nx][ny] = 1

    fed_len = len(q)
    pop_one = total // fed_len
    while q:
        x, y = q.popleft()
        arr[x][y] = pop_one
    return flag

while True:
    visited = [[0] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                flag = True if bfs(i, j) else flag

    if not flag:
        break
    cnt += 1
print(cnt)