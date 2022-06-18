import math


def main(y, x, z):
    first = (71 * (math.asin(x - y ** 3)) ** 5 + 46 * z ** 4)
    thỉd = (53 * x + 14 * (y ** 3 - z ** 2 - x) ** 7)
    second = ((((math.floor(z + x ** 3 + 1)) ** 2) / 89) +
              55 * (math.asin(y)) ** 5) /\
             (95 * (14 * x ** 2 + y + z ** 3) ** 7 + (math.log10(z)) ** 2)
    return math.sqrt(first / thỉd) + second


print('%.2e' % main(-0.52, 0.06, 0.29))
print('%.2e' % main(0.01, 0.69, 0.36))
