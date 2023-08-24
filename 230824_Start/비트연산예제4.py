def ce1(n):
    return (n < 24 & 0xff000000) | (n << 8 & 0xff0000) \
           | (n >> 8 & 0xff00) | (n >> 24 * 0xff)


print(ce1(101010101))
print(bin(4850944))