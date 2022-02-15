# Задача 11
import random
def fast_mul_gen(x, y):
    s = 0
    print('Result =', s)
    while x:
        if x % 2 != 0:
            print('Result =', s, '+', y)
            s = y + s
        print('y = y +', y)
        x = x // 2
        y = y * 2
    print('Result =', s)

def random_number():
	x = random.randint(1, 9)
	return x
for i in range(3):
    print('.......Test №', i )
    x = random_number()
    y = random_number()
    print('x =', x)
    print('y =', y)
    print('Function test fast_mul_gen()')
    fast_mul_gen(x, y)