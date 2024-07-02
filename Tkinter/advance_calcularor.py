import tkinter as tk
import math


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Calculator")

        # Entry Field
        self.entry = tk.Entry(master, width=25, font=("Arial", 14))
        self.entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('(', 5, 0), (')', 5, 1), ('sqrt', 5, 2), ('^', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('log', 6, 3),
            ('Clear', 7, 0), ('Clear All', 7, 1)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(master, text=text, width=5, height=2, font=("Arial", 12),
                            command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, value):
        if value == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")

        elif value == "Clear":
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text[:-1])

        elif value == "Clear All":
            self.entry.delete(0, tk.END)

        elif value == "sqrt":
            try:
                result = math.sqrt(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")

        else:
            self.entry.insert(tk.END, value)


def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
