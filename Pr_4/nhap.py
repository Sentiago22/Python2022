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


def change_color():
    global color
    new_color = yield #Returns the value of the function without destroying the state of the variables in the function
    color = new_color
    nb = yield
    return nb


def stop_drawing():
    while True:
        nb = yield
        if nb == 240:
            return 240


def draw_conner_y():
    x1 = yield
    y1 = yield
    while True:
        y2 = yield
        if y2 >= 240:
            return y2
        draw_line([(x1, y1), (x1, y2)], color)
        y1 = y2
        x2 = yield
        if x2 >= 240:
            return x2
        draw_line([(x1, y1), (x2, y1)], color)
        x1 = x2


def draw_conner_x():
    global color
    x1 = yield
    y1 = yield
    while True:
        x2 = yield
        if x2 >= 240:
            return x2
        draw_line([(x1, y1), (x2, y1)], color)
        x1 = x2
        y2 = yield
        if y2 >= 240:
            return y2
        draw_line([(x1, y1), (x1, y2)], color)
        y1 = y2


def draw_long_line():
    global color
    x1 = yield
    y1 = yield
    while True:
        x2 = yield
        if x2 >= 240:
            return x2
        y2 = yield
        if y2 >= 240:
            return y2
        draw_line([(x1, y1), (x2, y2)], color)
        x1 = x2
        y1 = y2


def draw_rel_line():
    global color
    x1 = yield
    y1 = yield
    while True:
        disp = yield

        if disp >= 240:
            return disp
        dx = ((disp & 240) >> 4) & 15
        dy = disp & 15
        if dx & 8:
            dx = (-1) * (dx & 7)
        if dy & 8:
            dy = (-1) * (dy & 7)
        draw_line([(x1, y1), (x1 + dx, y1 + dy)], color)
        x1 += dx
        y1 += dy

'''
def fill():
    nb = yield
    while nb // 10 != 24:
        nb = yield
'''

def main_gen():
    nb = yield
    while True:
        if nb == 255:
            return
        elif nb == 240:
            nb = yield from change_color()
        elif nb == 241:
            nb = yield from stop_drawing()
        elif nb == 242:
            nb = yield
        elif nb == 244:
            nb = yield from draw_conner_y()
        elif nb == 245:
            nb = yield from draw_conner_x()
        elif nb == 246:
            nb = yield from draw_long_line()
        elif nb == 247:
            nb = yield from draw_rel_line()
        else:
            nb = yield


def draw(pic):
    g = main_gen()
    next(g)
    for nb in pic:
        g.send(nb)


def draw_line(coords, color_index):
    canvas.create_line(*[(x * SCALE_X, y * SCALE_Y) for x, y in coords],
                       fill='#%02x%02x%02x' % COLORS[color_index], width=4)


color = 0
pic = Path('data/PIC.1').read_bytes()
print([hex(i) for i in pic])
canvas = tk.Canvas(width=160 * SCALE_X, height=170 * SCALE_Y)
canvas.pack()
draw(pic)
tk.mainloop()