def get_f(sy, sx):
    ret = 0
    for y in range(m):
        for x in range(m):
            ret += flies[sy + y][sx + x]
    return ret

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    flies = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        flies[i] = list(map(int, input().split()))

    max_f = 0
    for y in range(n - m + 1):
        for x in  range(n - m + 1):
            f = get_f(y, x)
            if f > max_f:
                max_f = f

    print('#{} {}'.format(test_case, max_f))
