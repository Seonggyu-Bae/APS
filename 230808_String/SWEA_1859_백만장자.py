T= int(input())

for tc in range(1,T+1):
    N = int(input())

    price_list = list(map(int, input().split()))
    len_Plist = len(price_list)

    max_price = 0
    max_profit = 0

    for i in range(-1,-len_Plist-1,-1):
        if price_list[i] >= max_price:
            max_price = price_list[i]

        else:
            max_profit += max_price - price_list[i]

    print(f'#{tc} {max_profit}')

