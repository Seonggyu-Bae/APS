for test_case in range(1, 11):
    N = int(input())
    height = list(map(int,input().split()))
    sum = 0
    for i in range(2,(N-2)):
        temp = max(height[i-1], height[i-2], height[i], height[i+1], height[i+2])
        if temp == height[i]:
            sum += temp - max(height[i-1], height[i-2], height[i+1], height[i+2])
    print(f'#{test_case} {sum}')