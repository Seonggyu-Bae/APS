# itoa() , atoi()

# 문자열을 숫자로 만듬 '123' >> 123
def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x) - ord('0')
    return i

# 숫자를 문자열로 만듬 123 >> '123'
def itoa(i):
    # 숫자 한자리를 때어서 문자로 만든다음 붙인다.
    result = ''
    while True:
        if i == 0:
            break
        result = chr(i%10 + ord('0')) + result
        i //= 10

    return result



print(type(itoa(123)))