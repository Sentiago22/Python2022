import math
def main(a, n, b, z):
    result = 0
    for i in range(1, b + 1):
        s = 0
        for c in range(1, n + 1):
            p = 0
            for k in range(1, a + 1):
                p += 47 * i ** 6 + 43 * math.exp(63 - 53 * k ** 2 - z ** 3) +\
                     64 * (math.log2(c)) ** 4
            s += p
        result += s
    return result

print('%.2e' % main(8, 3, 6, 0.63))
print('%.2e' % main(7, 3, 8, 0.75))
