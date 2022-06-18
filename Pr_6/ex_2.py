def person(name="", age=""):
    return name, age


def replace(pers, param, new):
    match param:
        case 'name':
            return person(name=new, age=pers[1])
        case 'age':
            return person(name=pers[0], age=new)
        case _:
            print("Something goes wrong")


def get(pers, param):
    match param:
        case 'name':
            print("name =", pers[0])
        case 'age':
            print("age =", pers[1])
        case _:
            print("Something goes wrong")


p1 = person(name='Минь', age=20)
print(p1)
p2 = replace(replace(p1, 'name', 'Алексей'), 'age', 21)
print(p2)
get(p1, 'name'), get(p1, 'age')
get(p2, 'name'), get(p2, 'age')
