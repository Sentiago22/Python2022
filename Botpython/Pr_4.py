import math


def main(n):
    if n == 0:
        return 0.02
    if n == 1:
        return 0.46
    if n >= 2:
        return 76 * math.atan(main(n - 1)) ** 2 - 1 - math.atan(main(n - 2))

print('%.2e' % main(8))
print('%.2e' % main(9))