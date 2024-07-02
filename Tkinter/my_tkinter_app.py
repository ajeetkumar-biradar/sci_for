import tkinter as tk
import requests


def get_quote():
    url = "https://api.quotable.io/random"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        quote = data["content"]
        author = data["author"]
        return f'"{quote}" - {author}'
    else:
        return "Failed to fetch quote"


def show_quote():
    quote = get_quote()

    quote_label.config(text=quote)


root = tk.Tk()

root.title("Quote of the Day")

root.geometry("400x200")

quote_label = tk.Label(root, text="", wraplength=300)
quote_label.pack(pady=20)

fetch_button = tk.Button(root, text="Fetch Quote", command=show_quote)
fetch_button.pack()

show_quote()

root.mainloop()
