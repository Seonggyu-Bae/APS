'''
1. 완전 탐색 접근
2. 가지치기(Bactracking)

---- 트리구조로 생각할 순 없을까? ( 이전 데이터를 봐야하는가? )

'''

T = int(input())


def dfs(month, acc_cost):
    global ans

    if month > 12:
        ans = min(ans, acc_cost)
        return

    if acc_cost > ans:
        return

    # 1일 이용권으로 모두 구입
    dfs(month + 1, acc_cost + months[month] * cost_day)
    # 1달 이용권 구입
    dfs(month + 1, acc_cost + cost_month)
    # 3달 이용권 구입
    dfs(month + 3, acc_cost + cost_month3)
    # 1년 이용권 구입
    dfs(month + 12, acc_cost + cost_year)


for tc in range(1, T + 1):
    cost_day, cost_month, cost_month3, cost_year = map(int, input().split())

    months = [0] + list(map(int, input().split()))
    ans = int(1e10)
    dfs(1, 0)
    print(f'#{tc} {ans}')
