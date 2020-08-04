T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    bus_stops = list(map(int, input().split()))
    energy = K
    ret = 0
    i = 0
    for p in range(1, N):
        energy -= 1
        if energy < 0:
           ret = 0
           break
        if p == bus_stops[i]:
            if i < M - 1 and bus_stops[i+1] - p > energy:
                energy = K
                ret += 1
            elif i == M - 1 and N - p > energy:
                energy = K
                ret += 1
            if i < M - 1:
                i += 1

    print('#{} {}'.format(test_case, ret))



