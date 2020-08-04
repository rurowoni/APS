for test_case in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))

    for _ in range(N):
        min_idx, max_idx = 0, 0
        for i in range(100):
            if heights[i] < heights[min_idx]:
                min_idx = i
            if heights[i] > heights[max_idx]:
                max_idx = i
        heights[max_idx] -= 1
        heights[min_idx] += 1
        if heights[max_idx] == heights[min_idx]:
            break

    min = 999
    max = 0
    for h in heights:
        if h < min:
            min = h
        if h > max:
            max = h
    print('#{} {}'.format(test_case, max - min))