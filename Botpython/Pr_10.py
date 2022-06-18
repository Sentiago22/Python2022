import re
import datetime as DT

table = [['1', 'eduard55[at]mail.ru', 'Эдуард Ш. Дисич', '15-09-2000'],
         ['0', 'vizko66[at]yandex.ru', 'Ян Д. Вицко', '19-07-2004'],
         [None, None, None, None],
         ['0', 'maksim55[at]gmail.com', 'Максим Н. Чабман', '27-02-2004']]


def main(table):
    table1 = [i for i in table if i != [None, None, None, None]]
    for i in range(len(table1)):
        if table1[i][0] == '1':
            table1[i][0] = 'Y'
        if table1[i][0] == '0':
            table1[i][0] = 'N'
        table1[i][1] = re.sub(r'\[at\]\w+\.+\w+', '', table1[i][1])
        table1[i][2] = re.sub(r'\w+\s+\w\.+\s', '', table1[i][2])
        date = DT.datetime.strptime(table1[i][3], '%d-%m-%Y').date()
        table1[i][3] = date.strftime('%y-%m-%d')
    return table1


print(main(table))

'''
from datetime import datetime


def change(s):
    s = list(filter(None, s))
    for i in range(len(s)):
        if '[' in s[i]:
            s[i] = s[i][:s[i].index('[')]
        elif '.' in s[i]:
            s[i] = s[i][:s[i].index('.') + 1]
        elif '1' == s[i]:
            s[i] = 'Y'
        elif '0' == s[i]:
            s[i] = 'N'
        elif '20' in s[i]:
            s[i] = s[i][:s[i].index('20'):] + s[i][-1]
            a = s[i] = s[i][:s[i].index('[')]
            b = s[i] = s[i][:s[i].index('.') + 1]
            c = s[i][:s[i].index('20'):] + s[i][-1]
            s[i] = a + b + c
    return s

def main(s):
    for i in range(len(s)):
        s[i] = change(s[i])
    s = list(filter(None, s))
    return s

print(main([['1', 'eduard55[at]mail.ru','Эдуард Ш. Дисич', '15-09-2000'],
            ['0', 'vizko66[at]yandex.ru','Ян Д. Вицко', '19-07-2004'],
            ['0', 'maksim55[at]gmail.com','Максим Н. Чабман', '27-02-2004']]))
'''

