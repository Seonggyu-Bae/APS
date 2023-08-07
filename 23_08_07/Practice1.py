# 문자열 뒤집기 (슬라이싱 안쓰고)
# 문자열의 길이가 N이라고 가정하면
# 0 <-> N-1
# 1 <-> N-2
# 2 <-> N-3
# 바꾸는 작업을 중간까지 하면 문자열이 뒤집힘 (0,N//2)

s = 'Reverse this string'
s = list(s)
N = len(s)
for i in range(0,N//2):
    # i번은 N-1-i번과 자리를 바꾸면 됨
    s[i],s[N-1-i] = s[N-1-i], s[i]


print(''.join(s))


"""is_true = True
for i in range(0,N//2):
    # i번은 N-1-i번과 자리를 바꾸면 됨
    if s[i] != s[N-1-i]:
        is_true = False
        break
"""