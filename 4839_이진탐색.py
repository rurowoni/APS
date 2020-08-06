def binary_search(target, l, r, c, cnt):
    if c == target:
        return cnt
    elif target < c:
        return binary_search(target, l, c, (l + c) // 2, cnt + 1)
    elif target > c:
        return binary_search(target, c, r, (r + c) // 2, cnt + 1)

T = int(input())

for test_case in range(1, T + 1):
    p, a, b = map(int, input().split())
    cnt_a = binary_search(a, 1, p, p // 2, 1)
    cnt_b = binary_search(b, 1, p, p // 2, 1)

    if cnt_a < cnt_b:
        result = 'A'
    elif cnt_a > cnt_b:
        result = 'B'
    else:
        result = 0

    print('#{} {}'.format(test_case, result))