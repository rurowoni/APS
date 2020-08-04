T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    n = list(map(int, input().split()))
    n_sum = [0] * N
    min = 1000001
    max = 0
    n_sum[0] = n[0]
    for i in range(N-1):
        n_sum[i+1] = n_sum[i] + n[i+1]
    for i in range(N - M + 1):
        sum = n_sum[i+M-1] - n_sum[i-1]
    print('#{} {}'.format(test_case, max-min))