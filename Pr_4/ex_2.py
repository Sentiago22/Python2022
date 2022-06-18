import math

class Math:
    def __init__(self, a, b, ):
        self.a = a
        self.b = b

    def pytago(self):
        c = math.sqrt(self.a ** 2 + self.b ** 2)
        return c

obj = Math(3, 4)
print('Variable of class Math:')
print(vars(obj))

while True:
    print('Enter the method to call. Press n to exit')
    s = input()
    if s == 'n':
        break
    print(getattr(obj, s)())