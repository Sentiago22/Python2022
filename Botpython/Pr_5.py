import math


def main(y, x, z):
    n = len(y)
    result = 0
    for i in range(1, n + 1):
        result += (59 * z[math.ceil(i/4 - 1)] ** 3 - 42 * y[i - 1] - x[i - 1] ** 2)\
                  ** 2
    return 46 * result

print('%.2e' % main([0.39, 0.17, 0.46], [-0.34, 0.95, 0.97], [-0.55, 0.79, -0.99]))
print('%.2e' % main([-0.25, 0.42, -0.96], [0.94, 0.67, 0.18], [-0.38, -0.8, -0.09]))