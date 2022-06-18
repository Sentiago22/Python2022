import math


def main(y):
    if y < 31:
        return (y ** 4 - (y - 9 * y ** 2 - 77 * y ** 3) ** 6 - y ** 2)
    if 31 <= y < 108:
        return ((35 * y ** 2) ** 6 - 1 - 27 * ((1 - y ** 3 - y ** 2)) ** 3)
    if y >= 108:
        return (y ** 21 + 2 * y ** 2)

print('%.2e' % main(75))
print('%.2e' % main(82))