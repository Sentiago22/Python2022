import random

names_list1 = ['Anh','Biên','Bách','Bằng','Cường','Cương','Hiếu','Hòa','Hoa','Hùng','Hồng']
names_list2 = ['Van','Minh','Tan','Binh','Phong']
a = int(input("input number:"))
i=0
while(i<a):
    first_name = input("Input first name: ")
    fullname = first_name+" "+random.choice(names_list1)+" "+random.choice(names_list2)
    print(fullname)
    i+=1
'''
import random


namePrefix = ["А", "Айне", "Арна", "Фионн", "Илле","Лианн", "Рис"]
namePostfix = ["долл", "ори", "аразу", "ссо", "гейт"]
surnamePrefix = ["Нум", "Онде", "Чор", "Вонд", "Сенв"]
surnamePostfix = ["ад", "дейх", "рок", "эйсайд", "зуст"]
intitial = ["А.", "Б.", "Д.", "С", "Ч."]

n = int(input())

for i in range (n):
    print(random.choice(namePrefix) + random.choice(namePostfix),random.choice(intitial), random.choice(surnamePrefix) + random.choice(surnamePostfix))

'''