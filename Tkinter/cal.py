import tkinter as tk
from tkinter import ttk, messagebox
import math


def calculate_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get()) / 100
        time = float(time_entry.get())

        if interest_type.get() == 1:
            simple_interest = (principal * rate * time) / 100
            result_message = f"Simple Interest: {simple_interest:.2f}"
        else:
            compound_interest = principal * math.pow((1 + rate), time)
            result_message = f"Compound Interest: {compound_interest:.2f}"

        messagebox.showinfo("Interest Calculation Result", result_message)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for Principal, Rate, and Time.")


root = tk.Tk()
root.title("Interest Calculator")

input_frame = ttk.Frame(root)
input_frame.pack(padx=20, pady=20)

ttk.Label(input_frame, text="Principal:").grid(row=0, column=0, padx=5, pady=5)
principal_entry = ttk.Entry(input_frame)
principal_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Rate (%):").grid(row=1, column=0, padx=5, pady=5)
rate_entry = ttk.Entry(input_frame)
rate_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Time (years):").grid(row=2, column=0, padx=5, pady=5)
time_entry = ttk.Entry(input_frame)
time_entry.grid(row=2, column=1, padx=5, pady=5)

interest_type = tk.IntVar()

simple_interest_radio = ttk.Radiobutton(input_frame, text="Simple Interest", variable=interest_type, value=1)
simple_interest_radio.grid(row=3, column=0, padx=5, pady=5)

compound_interest_radio = ttk.Radiobutton(input_frame, text="Compound Interest", variable=interest_type, value=2)
compound_interest_radio.grid(row=3, column=1, padx=5, pady=5)

calculate_button = ttk.Button(input_frame, text="Calculate Interest", command=calculate_interest)
calculate_button.grid(row=4, columnspan=2, padx=5, pady=10)

root.mainloop()