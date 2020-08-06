def count_mine(y, x):
    cnt = 0
    for dir in range(8):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue
        if map_mine[ny][nx] == '*':
            cnt += 1
    if cnt == 0:
        for dir in range(8):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            count_mine(ny, nx)
    map_mine[y][x] = cnt

def click(y, x):
    if map_mine[y][x] == '.':
        count_mine(y, x)


dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    map_mine = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        map_mine[i] = list(input())

    cy, cx = map(int, input().split())
    click(cy, cx)
    print(map_mine)

    result = 0
    print('#{} {}'.format(test_case, result))
