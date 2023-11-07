import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

info = {}
for _ in range(N):
    url, password = input().rstrip().split()
    info[url] = password

for _ in range(M):
    find = input().rstrip()
    print(info[find])
