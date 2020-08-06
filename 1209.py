def rotate(numbers):
    new_numbers = [[0 for x in range(100)] for y in range(100)]
    for y in range(100):
        for x in range(100):
            new_numbers[y][x] = numbers[x][y]
    return new_numbers

T = 10
for test_case in range(T):
    test_case = int(input())
    numbers = [[0 for x in range(100)] for y in range(100)]
    for i in range(100):
        numbers[i] = list(map(int, input().split()))

    result = 0
    for number in numbers:  # 행의 합
        total = sum(number)
        result = max(result, total)

    numbers = rotate(numbers)  # 회전

    for number in numbers:  # 열의 합
        total = sum(number)
        result = max(result, total)

    for y in range(100):  # 대각선의 합
        sum1, sum2 = 0, 0
        sum1 += numbers[y][y]
        sum2 += numbers[99 - y][y]
        result = max(result, sum1, sum2)

    print('#{} {}'.format(test_case, result))