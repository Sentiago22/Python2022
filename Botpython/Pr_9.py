class main:
    def __init__(self):
        self.condition = 'A'

    def walk(self):
        if self.condition == 'A':
            self.condition = 'B'
            return 0
        elif self.condition == 'B':
            self.condition = 'C'
            return 1
        elif self.condition == 'C':
            self.condition = 'C'
            return 4
        elif self.condition == 'F':
            self.condition = 'H'
            return 8
        elif self.condition == 'G':
            self.condition = 'B'
            return 10
        else:
            raise KeyError

    def draw(self):
        if self.condition == 'C':
            self.condition = 'D'
            return 2
        elif self.condition == 'E':
            self.condition = 'F'
            return 6
        elif self.condition == 'F':
            self.condition = 'G'
            return 7
        elif self.condition == 'G':
            self.condition = 'H'
            return 9
        elif self.condition == 'H':
            self.condition = 'C'
            return 11
        else:
            raise KeyError

    def throw(self):
        if self.condition == 'C':
            self.condition = 'F'
            return 3
        elif self.condition == 'D':
            self.condition = 'E'
            return 5
        else:
            raise KeyError

o = main()
print(o.walk()) # 0
print(o.walk()) # 1
print(o.throw()) # 3
print(o.walk()) # 8
print(o.draw()) # 11
print(o.throw()) # 3
print(o.throw()) # KeyError
print(o.draw()) # 7
print(o.draw()) # 9
print(o.draw()) # 11
print(o.walk()) # 4
print(o.walk()) # 4
print(o.draw()) # 2
print(o.throw()) # 5
print(o.draw()) # 6
print(o.draw()) # 7
print(o.walk()) # 10