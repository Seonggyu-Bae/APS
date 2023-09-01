def solve(idx, lst):  # lst : 선택한 신청서 목록
    global max_cnt

    if idx == N:
        # 시간이 겹치는지 검사
        end = 0
        for e in lst:
            if e[0] < end:  # 겹침
                break
            end = e[1]
        else:   # break 한번도 수행 안된경우 ( 안겹친경우)
            if max_cnt < len(lst):
                max_cnt = len(lst)
        return

    lst.append(app_form[idx])
    solve(idx + 1, lst)
    lst.pop()
    solve(idx+1, lst)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    count = 1
    app_form = [list(map(int, input().split())) for _ in range(N)]

    app_form.sort(key=lambda x: x[1])
    max_cnt = 0
    solve(0,[])

    print(max_cnt)