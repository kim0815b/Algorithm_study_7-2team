arr = [list(map(int,input())) for _ in range(9)]

box_list = [[0] * 9 for _ in range(9)]
col_list = [[0] * 9 for _ in range(9)]
row_list = [[0] * 9 for _ in range(9)]

box_num = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

for i in range(9):
    for j in range(9):
        if arr[i][j]:
            row_list[i][arr[i][j] - 1] = 1
            col_list[j][arr[i][j] - 1] = 1
            box_list[box_num[i // 3][j // 3]][arr[i][j] - 1] = 1

result = []
def get_sudoku(x, y):
    if result:
        return
    if y == 9:
        x += 1
        y = 0
    if x == 9:
        result.append([[num for num in row] for row in arr])
        return
    if not arr[x][y]:
        for num in range(9):
            if is_valid(x, y, num):
                get_sudoku(x, y+1)
                row_list[x][num] = 0
                col_list[y][num] = 0
                box_list[box_num[x // 3][y // 3]][num] = 0
                arr[x][y] = 0
    else:
        get_sudoku(x, y+1)
    return

def is_valid(x, y, num):
    if row_list[x][num]: #행 탐색
        return False
    if col_list[y][num]:
        return False
    if box_list[box_num[x // 3][y // 3]][num]:
        return False
    row_list[x][num] = 1
    col_list[y][num] = 1
    box_list[box_num[x // 3][y // 3]][num] = 1
    arr[x][y] = num + 1
    return True

get_sudoku(0, 0)

for i in result[0]:
    print(*i, sep='')
