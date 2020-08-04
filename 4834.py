T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    numbers = input()
    counts = [0] * 10
    max_idx = 9
    for number in numbers:
        idx = int(number)
        counts[idx] += 1
        if counts[idx] > counts[max_idx]:
            max_idx = idx
        elif counts[idx] == counts[max_idx] and idx > max_idx:
            max_idx = idx
    print('#{} {} {}'.format(test_case, max_idx, counts[max_idx]))