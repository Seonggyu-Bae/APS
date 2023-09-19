# {1, 2, 3} 집합에서 3개의 숫자를 선택하는 기본적인 예제

arr = [i for i in range(1, 11)]
path = [0] * len(arr)

def backtracking(cnt,set_sum):
    # 기저 조건 : 숫자 3개를 골랐을 때 종료

    if set_sum == 10:
        print(path)
        return

    for num in arr:
        # 가지치기 : 중복된 숫자 제거
        if num in path or set_sum > 10:
            continue
        # 들어가기 전 로직 : 경로 저장
        path[cnt] = num
        set_sum += num
        # 다음 재귀 함수 호출
        backtracking(cnt + 1,set_sum)

        # 돌아와서 할 행동 : 초기화
        path[cnt] = 0
        set_sum -= num


backtracking(0,0)