# Задача 10
import random
def fast_mul(x, y):
	s = 0
	while x:
		if x % 2 != 0:
			s = y + s
		x = x // 2
		y = y * 2
	return s

def fast_pow(x, y):
	s = 0
	if (y == 0):
		s = 1
	if (y == 1):
		s = x
	y = y - 1
	z = x
	x1 = x
	while y:
		s = 0
		while x:
			if x % 2 != 0:
				s = x1 + s
			x = x // 2
			x1 = x1 * 2
		x = s
		x1 = z
		y = y - 1
	return s

def random_number():
	x = random.randint(1, 9)
	return x
for i in range(3):
	print('.......Test №', i )
	x = random_number()
	y = random_number()
	print('x =', x)
	print('y =', y)
	print('Multiplication result:', fast_mul(x, y))
	print('Result', x, 'degree of', y, ':', fast_pow(x, y))
