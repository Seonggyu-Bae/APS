N, M, B = map(int, input().split()) # B: 보유블록개수

land_height = [list(map(int, input().split())) for _ in range(N)]

total = 0
avg = 0

for x in land_height:
    for y in x:
        total += y

avg = total/(M*N)
print(avg)


# 2초 : 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
# 1초 : 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.