T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    numbers = range(1, 13)

    result = 0
    for i in range(1 << 12):
        sub = []
        for j in range(12):
            if i & (1 << j):
                sub.append(numbers[j])
        if len(sub) == n and sum(sub) == k:
            result += 1

    print('#{} {}'.format(test_case, result))