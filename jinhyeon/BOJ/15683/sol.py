n, m = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

# 상 하 좌 우
dxl = [-1, 1, 0, 0]
dyl = [0, 0, -1, 1]

# 1번 상 하 좌 우
# 2번 0 좌 우 1 상 하
# 3번 0 상 우 1 우 하 2 하 좌 3 좌 상
dire = [0,
        [[0], [1], [2], [3]],
        [[2, 3], [0, 1]],   #, [2, 3], [0, 1]
        [[0, 3], [3, 1], [1, 2], [2, 0]],
        [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 1, 3]],
        [[0, 1, 2, 3]]  # , [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]
]
cctv = []
ans = float('inf')
blind_spot = 0
for i in range(n):
    for j in range(m):
        if 0 < arr[i][j] < 6:
            cctv.append(arr[i][j])
        elif arr[i][j] == 0:
            blind_spot += 1

def comb(idx, path):
    if idx == len(cctv):    #모든 cctv 탐색
        global ans
        ans = min(ans, scan_cctv(path))
        return
    for i in range(len(dire[cctv[idx]])):   #각 dire길이 만큼 (cctv의 방향 경우의 수)
        path.append(i)
        comb(idx + 1, path)
        path.pop()

def scan_cctv(path):
    idx = 0
    cur_blind_spot = blind_spot
    visited = [[num for num in col] for col in arr]

    for i in range(n):
        for j in range(m):
            if 0 < arr[i][j] < 6:
                k = dire[arr[i][j]][path[idx]]   # 탐색해야할 방향의 dxy 인덱스 번호를 모아둔
                for l in k:
                    cnt = 1
                    while True:
                        x, y = i + dxl[l] * cnt, j + dyl[l] * cnt
                        if not (0 <= x < n and 0 <= y < m) or arr[x][y] == 6:
                            break   #벽을 만나면 그 방향은 탐색 종
                        if arr[x][y] == 0 and visited[x][y] == 0:
                            visited[x][y] = 1
                            cur_blind_spot -= 1
                        cnt += 1
                idx += 1
    return cur_blind_spot

comb(0, [])
print(ans)