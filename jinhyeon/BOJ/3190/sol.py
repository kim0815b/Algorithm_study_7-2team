import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
k = int(input())
dxl = [0, 0, 1, -1] #동 서 남 북
dyl = [1, -1, 0, 0]
left = [3, 2, 0, 1]
right = [2, 3, 1, 0]
arr = [[0] * n for _ in range(n)]   #게임 판
for _ in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 2   # 사과 설정
l = int(input())
dq = deque()
for _ in range(l):
    c, d = input().split()
    dq.append((int(c), d))  #방향 전환 정보 큐에 담기

cnt = 1
x, y, d = 0, 0, 0
snake = deque()
snake.append((x, y))
arr[x][y] = 1
next_c = dq[0][0]
while True:
    x, y = x + dxl[d], y + dyl[d]
    if not(0 <= x < n and 0 <= y < n):
        break
    if arr[x][y] == 1:
        break
    snake.append((x, y))    # 머리를 내민다
    if arr[x][y] == 0:
        tx, ty = snake.popleft()    #꼬리를 뺀다
        arr[tx][ty] = 0
    arr[x][y] = 1   # 머리 차지

    if dq and cnt == dq[0][0]:
        next_c, dire_char = dq.popleft()
        d = left[d] if dire_char == 'L' else right[d]   # 방향 전환
    cnt += 1

print(cnt)