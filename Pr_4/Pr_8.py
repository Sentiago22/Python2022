from pathlib import Path
import tkinter as tk

SCALE_X = 6
SCALE_Y = 4

COLORS = [
    (0, 0, 0),
    (0, 0, 168),
    (0, 168, 0),
    (0, 168, 168),
    (168, 0, 0),
    (168, 0, 168),
    (168, 84, 0),
    (168, 168, 168),
    (84, 84, 84),
    (84, 84, 252),
    (84, 252, 84),
    (84, 252, 252),
    (252, 84, 84),
    (252, 84, 252),
    (252, 252, 84),
    (252, 252, 252)
]


# 0xf4
def y_corner(picArr, index):
    global color
    index += 1
    x1 = picArr[index]
    index += 1
    y1 = picArr[index]
    index += 1
    while True:
        y2 = picArr[index]
        index += 1
        if y2 >= 240:
            break
        draw_line([(x1, y1), (x1, y2)], color)
        y1 = y2
        x2 = picArr[index]
        index += 1
        if x2 >= 240:
            break
        draw_line([(x1, y1), (x2, y1)], color)
        x1 = x2
    return index - 1


# 0xf5
def x_corner(picArr, index):
    global color
    index += 1
    x1 = picArr[index]
    index += 1
    y1 = picArr[index]
    index += 1
    while True:
        x2 = picArr[index]
        index += 1
        if x2 >= 240:
            break
        draw_line([(x1, y1), (x2, y1)], color)
        x1 = x2
        y2 = picArr[index]
        index += 1
        if y2 >= 240:
            break
        draw_line([(x1, y1), (x1, y2)], color)
        y1 = y2
    return index - 1


# 0xf6
def absolute_line(picArr, index):
    global color
    index += 1
    x1 = picArr[index]
    index += 1
    y1 = picArr[index]
    index += 1
    while True:
        x2 = picArr[index]
        index += 1
        if x2 >= 240:
            break
        y2 = picArr[index]
        index += 1
        if y2 >= 240:
            break
        draw_line([(x1, y1), (x2, y2)], color)
        x1 = x2
        y1 = y2
    return index - 1


# 0xf7
def relative_line(picArr, index):
    global color
    index += 1
    x1 = picArr[index]
    index += 1
    y1 = picArr[index]
    index += 1
    while True:
        disp = picArr[index]
        index += 1
        if disp >= 240:
            break
        dx = ((disp & 240) >> 4) & 15
        dy = disp & 15
        if dx & 8:
            dx = (-1) * (dx & 7)
        if dy & 8:
            dy = (-1) * (dy & 7)
        draw_line([(x1, y1), (x1 + dx, y1 + dy)], color)
        x1 += dx
        y1 += dy
    return index - 1


def wait240(picArr, index):
    index += 1
    while picArr[index] != 240 and picArr[index] != 255:
        index += 1
    return index


def wait24_(picArr, index):
    index += 1
    while picArr[index] // 10 != 24:
        index += 1
    return index


def draw_line(coords, color_index):
    canvas.create_line(*[(x * SCALE_X, y * SCALE_Y) for x, y in coords],
                       fill='#%02x%02x%02x' % COLORS[color_index], width=4)


def draw(pic):
    global color
    picArr = [i for i in pic]
    i = 0
    while i < len(picArr):
        if picArr[i] == 255:
            return
        if picArr[i] == 240:
            print("КАРТИНКУ ВКЛЮЧИЛ ЦВЕТ ПОМЕНЯЛ", picArr[i], i)
            print("ЦВЕТ КАРТИНКИ", picArr[i], i + 1)
            color = picArr[i + 1]
            i += 2
        elif picArr[i] == 241:
            print("ОФФ КАРТИНКИ", picArr[i], i)
            while i < len(picArr) and picArr[i] != 240:
                i += 1
        elif picArr[i] == 242:
            print("ПРИОРИТЕТ ВКЛЮЧИЛ ЦВЕТ ПОМЕНЯЛ", picArr[i], i)
            print("ЦВЕТ ПРИОРИТЕТ", picArr[i], i + 1)
            i += 2
        elif picArr[i] == 243:
            print("ОФФ ПРИОРИТЕТ", picArr[i], i)
            i += 1
        elif picArr[i] == 244:
            print("ВЕРТИКАЛЬНЫЙ УГОЛ", picArr[i], i)
            i = y_corner(picArr, i)
        elif picArr[i] == 245:
            print("ГОРИЗОНТАЛЬНЫЙ УГОЛ", picArr[i], i)
            i = x_corner(picArr, i)
        elif picArr[i] == 246:
            print("ДЛИННЫЕ ЛИНИИ", picArr[i], i)
            i = absolute_line(picArr, i)
        elif picArr[i] == 247:
            print("КОРОТКИЕ ЛИНИИ", picArr[i], i)
            i = relative_line(picArr, i)
        elif picArr[i] == 248:
            print("ЗАЛИЛ", picArr[i], i)
            i = wait24_(picArr, i)
        else:
            i += 1


color = 0
pic = Path('data/PIC.2').read_bytes()
print([hex(i) for i in pic])
canvas = tk.Canvas(width=160 * SCALE_X, height=170 * SCALE_Y)
canvas.pack()
draw(pic)
tk.mainloop()