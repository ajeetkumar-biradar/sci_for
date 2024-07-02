import tkinter as tk
from tkinter import colorchooser


def use_pen():
    global tool
    tool = "pen"


def use_brush():
    global tool
    tool = "brush"


def choose_color():
    global pen_color
    color = colorchooser.askcolor()
    if color:
        pen_color = color[1]


def use_eraser():
    global tool
    tool = "eraser"


def change_size(value):
    global brush_size
    brush_size = int(value)


def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    if tool == "pen":
        canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline="")
    elif tool == "brush":
        canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline="")
    elif tool == "eraser":
        canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="")


root = tk.Tk()
root.title("Simple Paint")

tools_frame = tk.Frame(root)
tools_frame.pack(side=tk.TOP, padx=5, pady=5)

pen_button = tk.Button(tools_frame, text="Pen", command=use_pen)
pen_button.pack(side=tk.LEFT, padx=5)

brush_button = tk.Button(tools_frame, text="Brush", command=use_brush)
brush_button.pack(side=tk.LEFT, padx=5)

color_button = tk.Button(tools_frame, text="Color", command=choose_color)
color_button.pack(side=tk.LEFT, padx=5)

eraser_button = tk.Button(tools_frame, text="Eraser", command=use_eraser)
eraser_button.pack(side=tk.LEFT, padx=5)

size_scale = tk.Scale(tools_frame, from_=1, to=20, orient=tk.HORIZONTAL, label="Size", command=change_size)
size_scale.pack(side=tk.LEFT, padx=5)

canvas = tk.Canvas(root, bg="white", width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind("<B1-Motion>", paint)

tool = "pen"
pen_color = "black"
brush_size = 5

root.mainloop()
