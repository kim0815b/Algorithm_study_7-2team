n = int(input())

arr = [input().split() for _ in range(n)]
dxl = [1, -1, 0, 0]
dyl = [0, 0, 1, -1]
t = []
ans = ''
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'T':
            t.append((i, j))

def comb(x, y, cnt):
    global ans
    if ans == 'YES':
        return
    if not cnt:
        ans = survilance()
        return
    if y == n:
        y = 0
        x += 1
    if x == n:  #사실 이 전에 리턴해야함  앞으로 남은 칸보다 cnt가 많을때
        return
    if arr[x][y] == 'X':
        arr[x][y] = 'O'
        comb(x, y+1, cnt-1)
        arr[x][y] = 'X'
    comb(x, y+1, cnt)

def survilance():
    for x, y in t:
        for dx, dy in zip(dxl, dyl):
            cnt = 1
            while True:
                nx, ny = x + dx * cnt, y + dy * cnt
                if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny] == 'O':
                    break
                if arr[nx][ny] == 'S':
                    return 'NO'
                cnt += 1
    return 'YES'

comb(0, 0, 3)
print(ans)
