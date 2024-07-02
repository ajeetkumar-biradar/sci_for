import tkinter as tk
from tkinter import messagebox


def add(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        return "Error"


def subtract(a, b):
    try:
        return float(a) - float(b)
    except ValueError:
        return "Error"


def multiply(a, b):
    try:
        return float(a) * float(b)
    except ValueError:
        return "Error"


def divide(a, b):
    try:
        if float(b) == 0:
            return "Error: Division by zero"
        return float(a) / float(b)
    except ValueError:
        return "Error"


def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)


def evaluate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")


def clear_display():
    display.delete(0, tk.END)


root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="sunken")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        if button_text == "=":
            button = tk.Button(root, text=button_text, font=("Arial", 18), command=evaluate)
        elif button_text == "C":
            button = tk.Button(root, text=button_text, font=("Arial", 18), command=clear_display)
        else:
            button = tk.Button(root, text=button_text, font=("Arial", 18),
                               command=lambda text=button_text: button_click(text))
        button.grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i + 1, weight=1)

clear_button = tk.Button(root, text="C", font=("Arial", 18), command=clear_display)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

root.mainloop()
