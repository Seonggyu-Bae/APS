import sys
input = sys.stdin.readline

N = int(input())

chat = [input().rstrip() for _ in range(N)]

cnt = 0
start = False
first = set()
for i in range(N):
    if chat[i] == 'ENTER':
        first = set()
    else:
        if chat[i] not in first:
            cnt +=1
            first.add(chat[i])


print(cnt)
