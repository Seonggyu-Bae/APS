import sys
from itertools import combinations

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    mbti = input().rstrip().split()
    ans = 0xfffffff
    check = list(combinations(mbti, 3))

    for c in check:
        if N > 48:
            ans = 0
            break
        temp = 0
        for i in range(3):
            for j in range(i+1, 3):
                for k in range(4):
                    if c[i][k] != c[j][k]:
                        temp += 1
        if temp == 0:
            ans = temp
            break
        if temp < ans:
            ans = temp
    print(ans)
    print(16**3)