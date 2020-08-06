T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    canvas = [[0 for x in range(10)] for y in range(10)]
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if canvas[r][c] == 0 or canvas[r][c] == color:
                    canvas[r][c] = color
                else:
                    canvas[r][c] = 3

    result = 0
    for y in range(10):
        for x in range(10):
            if canvas[y][x] == 3:
                result += 1

    print('#{} {}'.format(test_case, result))