def Power(Base, Exponent):
    global cnt1
    if Base == 0:
        cnt1 += 1
        return 1

    result = 1 # Base^0는 1이므로
    for i in range(Exponent):
        cnt1 += 1
        result *= Base

    return result


def Power1(Base, Exponent):
    global cnt2
    cnt2 += 1
    if Exponent == 0 or Base == 0:
        return 1

    if Exponent % 2 == 0:
        NewBase = Power1(Base, Exponent / 2)
        return NewBase * NewBase

    else:
        NewBase = Power1(Base, (Exponent - 1) / 2)
        return (NewBase * NewBase) * Base
cnt1 = 0
cnt2 = 0

print(Power(2,100),cnt1)

print(Power1(2,100),cnt2)