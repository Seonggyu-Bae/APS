def bs(s, e, find_arr, target,idx):
    global is_right, is_left
    start = s
    end = e
    if s > e:
        return False
    else:
        mid = (start+end)//2
        if find_arr[mid] == target:
            if idx <=1:
                is_left = True
                is_right = True
            return True
        elif find_arr[mid] > target:
            if is_left:
                return False
            is_left = True
            is_right = False
            return bs(s,mid-1,find_arr,target,idx+1)
        else:
            if is_right:
                return False
            is_right = True
            is_left = False
            return bs(mid+1,end,find_arr,target,idx+1)



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    count = 0
    for element in B:
        is_right = False
        is_left = False
        find = bs(0,N-1,A,element,0)
        if find:
            count += 1

    print(f'#{tc} {count}')