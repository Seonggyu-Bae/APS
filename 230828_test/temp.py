T = int(input())

for _ in range(T):
    tc = int(input())
    s_list = list(map(int, input().split()))
    score_freq = [0] * 101
    s_max = 0
    max_freq = 0

    for s in s_list:
        score_freq[s] += 1

    for i in range(1, 101):
        if score_freq[i] >= max_freq:
            max_freq = score_freq[i]
            s_max = i

    print(f'#{tc} {s_max}')