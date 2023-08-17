def baby_gin(my_list):
    count = [0] * 10

    for i in my_list:
        count[i] += 1

    # find triplet
    for i in range(len(count)):
        if count[i] >= 3:
            count[i] -= 3

    # find run
    for _ in range(2):
        for i in range(len(count)-2):
            if count[i] >= 1:
                if count[i+1] >=1 and count[i+2] >=1:
                    count[i] -= 1
                    count[i+1] -= 1
                    count[i+2] -= 1

    for i in range(len(count)):
        if count[i]!=0:
            return False

    return True

a = []
print(baby_gin(a))



