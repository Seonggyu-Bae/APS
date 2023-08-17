def fibo1(n):
    global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = (fibo1(n-1) + fibo1(n-2))
    return memo[n]

n = 4
memo = [0] * (n+1)
memo[1] = 1
#print(fibo1(n))
fibo1(n)
print(memo)

new = [[0]* n for _ in range(n)]
new[0][0] = 1
def pascal(n):
    global new
    for i in range(1,n):
        for j in range(i+1):
            if j-1 >= 0:
                new[i][j] = (new[i-1][j-1] + new[i-1][j])
            else:
                new[i][j] = new[i - 1][j]



pascal(4)
print(f'#1')
for i in range(0,4):
    for j in range(i+1):
        print(new[i][j],end=' ')
    print()
