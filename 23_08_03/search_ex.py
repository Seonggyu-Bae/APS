# a가 정렬되어있지않다면
def sequentialsearch1(a, n, key): # a: 배열, n:배열의 길이, key: 찾는 값
    i = 0
    while i < n and a[i] != key:
        i = i+1
    if i<n:
        return i
    else:
        return -1

#a가 오름차순으로 정렬되어있다면
def seqeuntialsearch2(a,n,key):
    i = 0
    while i < n and a[i] < key:
        i = i + 1
    if i < n and a[i] == key:
        return i
    else:
        return -1