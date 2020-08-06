T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))

    result = []
    for i in range(10):
        sw = i
        for j in range(i, n):
            if i % 2 == 0 and numbers[j] > numbers[sw]:
                sw = j
            elif i % 2 and numbers[j] < numbers[sw]:
                sw = j
        numbers[i], numbers[sw] = numbers[sw], numbers[i]

    print('#{}'.format(test_case), end = ' ')
    for i in range(10):
        print(numbers[i], end = ' ')
    print()