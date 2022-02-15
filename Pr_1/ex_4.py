#exercise_4
def e4_1(x):
	x = x + x #2
	x = x + x #4
	x = x + x + x #12
	return(x)

def e4_2(x):
	x = x + x #2
	x = x + x #4
	x = x + x #8
	x = x + x #16
	return(x)

def e4_3(x):
	x = c #1
	z = c #1
	x = x + x #2
	x = x + x #4
	y = x + x #8
	x = z - y #-7
	x = y - x #15
	return(x)

def e4_4(x):
	# Задание 4
	x = c #1
	x = x + x #2
	x = x + x #4
	x = x + x #8
	x = x - c #7
	x = x + x #14
	x = x + x #28
	x = x + c #29
	return(x)

c = int(input())
print(c, '* 12 =', e4_1(c))
print(c, '* 16 =', e4_2(c))
print(c, '* 15 =', e4_3(c))
print(c, '* 29 =', e4_4(c))