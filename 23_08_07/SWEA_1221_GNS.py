T = int(input())

for _ in range(1,1+T):
    tc,s_len = map(str,input().split())
    my_str = str(input())
    counting = [0] * 10
    a = my_str.split(' ',int(s_len))
    temp = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    for num in a:
        if num == 'ZRO':
            counting[0] += 1
        elif num == 'ONE':
            counting[1] += 1
        elif num == 'TWO':
            counting[2] += 1
        elif num == 'THR':
            counting[3] += 1
        elif num == 'FOR':
            counting[4] += 1
        elif num == 'FIV':
            counting[5] += 1
        elif num == 'SIX':
            counting[6] += 1
        elif num == 'SVN':
            counting[7] += 1
        elif num == 'EGT':
            counting[8] += 1
        else:
            counting[9] += 1
    print(tc)
    for i in range(10):
        for j in range(counting[i]):
            print(temp[i],end=' ')
    print()