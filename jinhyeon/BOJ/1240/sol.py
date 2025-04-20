from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, w = map(int, input().split())
    tree[a].append((b, w))
    tree[b].append((a, w))

def bfs(a, b):
    visited = [0] * (n + 1)
    dq = deque()
    dq.append(a)
    visited[a] = 1
    while dq:
        node = dq.popleft()
        if node == b:
            return visited[node]-1
        for next_n, w in tree[node]:
            if visited[next_n]: continue
            dq.append(next_n)
            visited[next_n] = visited[node] + w
    return -1
ans = []
for _ in range(m):
    a, b = map(int, input().split())
    ans.append(bfs(a, b))
print(*ans, sep='\n')