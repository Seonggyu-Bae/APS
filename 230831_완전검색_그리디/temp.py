# 단순히 가장 높은 수 중 가장 오른쪽에 있는수를 앞에 있는 수와 바꾸면 되는게 아님
# 32888 2  같은건 88832가 나와야 하지만 88823가 나옴

# 교환을 통한 순열 만들기
# idx 번째 요소를 본인 포함(자리 안바꾸는거) 뒤쪽요소와 자리 바꿔보기

def make_perm2(idx, origin, cnt):
    if cnt > len(origin) == idx:
        a.append([*origin])
    if idx == cnt:
        a.append([*origin])
        pass

    for i in range(idx, len(origin)):
        origin[idx], origin[i] = origin[i], origin[idx]
        make_perm2(idx + 1, origin, cnt)
        # 자리 다시 돌려놓기
        origin[idx], origin[i] = origin[i], origin[idx]



T = int(input())

for tc in range(1, T + 1):
    info, cnt = input().split()
    info, cnt = list(info), int(cnt)
    a = []
    m_value = 0
    make_perm2(0, info, cnt)
    for i in range(len(a)):
        b = ''
        for k in range(len(info)):
            b += a[i][k]
        val = int(b)
        if val > m_value:
            m_value = val
    print(f'#{tc} {m_value}')
