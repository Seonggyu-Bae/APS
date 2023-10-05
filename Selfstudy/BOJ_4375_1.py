while True:
    try:
        N = int(input())
    except:
        break

    ans = 1
    while True:
        if ans % N == 0:
            print(len(str(ans)))
            break
        else:
            ans = ans*10 + 1
