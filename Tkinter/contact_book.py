import tkinter as tk
from tkinter import messagebox


class ContactBook:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")

        self.contacts = []

        tk.Label(master, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(master, text="Phone:").grid(row=1, column=0, padx=5, pady=5)

        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(master, text="Add Contact", command=self.add_contact).grid(row=2, column=0, columnspan=2, padx=5,
                                                                             pady=5, sticky="we")
        tk.Button(master, text="Edit Contact", command=self.edit_contact).grid(row=3, column=0, columnspan=2, padx=5,
                                                                               pady=5, sticky="we")
        tk.Button(master, text="View Contact", command=self.view_contact).grid(row=4, column=0, columnspan=2, padx=5,
                                                                               pady=5, sticky="we")
        tk.Button(master, text="Reset Fields", command=self.reset_fields).grid(row=5, column=0, columnspan=2, padx=5,
                                                                               pady=5, sticky="we")
        tk.Button(master, text="Exit", command=self.master.quit).grid(row=6, column=0, columnspan=2, padx=5, pady=5,
                                                                      sticky="we")

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            self.contacts.append((name, phone))
            messagebox.showinfo("Success", "Contact added successfully.")
            self.reset_fields()
        else:
            messagebox.showerror("Error", "Please enter both name and phone number.")

    def edit_contact(self):
        selected_contact = self.get_selected_contact()
        if selected_contact:
            name, phone = selected_contact
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)
            self.phone_entry.insert(0, phone)

    def view_contact(self):
        selected_contact = self.get_selected_contact()
        if selected_contact:
            name, phone = selected_contact
            messagebox.showinfo("Contact Details", f"Name: {name}\nPhone: {phone}")

    def get_selected_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            return (name, phone)
        else:
            messagebox.showerror("Error", "Please select a contact.")
            return None

    def reset_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    contact_book = ContactBook(root)
    root.mainloop()


if __name__ == "__main__":
    main()
