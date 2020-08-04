T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    L = list(map(int, input().split()))
    min = 1000001
    max = 0
    for i in L:
        if i < min:
            min = i
        if i > max:
            max = i

    print('#{}'.format(test_case), max - min)