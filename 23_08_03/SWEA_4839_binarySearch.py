def my_bserach(last, key):
    first = 1
    end = last
    count = 0
    while first <= end:
        mid = int((first + end) / 2)
        count += 1
        if mid > key:
            end = mid
        elif mid < key:
            first = mid
        if mid == key:
            return count

    return False


T = int(input())

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())

    if my_bserach(P, A) < my_bserach(P, B):
        print(f'#{tc} A')
    elif my_bserach(P, A) > my_bserach(P, B):
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')
