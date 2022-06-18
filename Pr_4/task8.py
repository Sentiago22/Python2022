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


def draw_line(coords, color_index):
    canvas.create_line(*[(x * SCALE_X, y * SCALE_Y) for x, y in coords],
                       fill='#%02x%02x%02x' % COLORS[color_index], width=4)


def draw_corner(args, color, isY=True):
    x, y = args[0], args[1]
    coords = [(x, y)]
    for i in range(2, len(args)):
        x, y = (x, args[i]) if isY else (args[i], y)
        isY = not isY
        coords.append((x, y))
    draw_line(coords, color)


def draw_abs(args, color):
    coords = [(args[0], args[1])]
    for i in range(2, len(args), 2):
        coords.append((args[i], args[i + 1]))
    draw_line(coords, color)


def draw_rel(args, color):
    x, y = args[0], args[1]
    coords = [(x, y)]
    for i in range(2, len(args)):
        xd, yd = args[i] >> 4 & 7, args[i] & 7
        xs, ys = args[i] >> 4 & 8, args[i] & 8
        x += -xd if xs else xd
        y += -yd if ys else yd
        coords.append((x, y))
    coords += coords if len(coords) == 1 else []
    draw_line(coords, color)


def draw(pic):
    commands = []
    index = -1
    for byte in pic:
        if byte >= 0xf0:
            commands.append([])
            index += 1
        commands[index].append(byte)
    piccolor = None
    picdraw = None
    for cmd in commands:
        action, args = cmd[0], cmd[1:]
        if action == 0xf0:  # Change picture color and enable picture draw
            picdraw = True
            piccolor = args[0]
        if action == 0xf1:  # Disable picture draw
            picdraw = False
        if action == 0xf4 and picdraw:  # Draw a Y corner
            draw_corner(args, piccolor, isY=True)
        if action == 0xf5 and picdraw:  # Draw an X corner
            draw_corner(args, piccolor, isY=False)
        if action == 0xf6 and picdraw:  # Absolute line
            draw_abs(args, piccolor)
        if action == 0xf7 and picdraw:  # Relative line
            draw_rel(args, piccolor)


pic = Path('data/PIC.1').read_bytes()
print('PIC.1')
canvas = tk.Canvas(width=160 * SCALE_X, height=170 * SCALE_Y)
canvas.pack()
draw(pic)
tk.mainloop()
