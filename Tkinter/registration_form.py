import tkinter as tk
from tkinter import messagebox


def register():
    name = entry_name.get()
    age = entry_age.get()
    gender = var_gender.get()
    address = text_address.get("1.0", tk.END)
    email = entry_email.get()
    contact = entry_contact.get()
    country = entry_country.get()
    state = entry_state.get()
    diseases = []
    if cold_var.get():
        diseases.append("Cold")
    if cough_var.get():
        diseases.append("Cough")
    if fever_var.get():
        diseases.append("Fever")
    diseases_text = ', '.join(diseases)

    message = f"Name: {name}\nAge: {age}\nGender: {gender}\nAddress: {address}\nEmail: {email}\nContact: {contact}\nCountry: {country}\nState: {state}\nDiseases: {diseases_text}"
    messagebox.showinfo("Registration Details", message)


root = tk.Tk()
root.title("COVID Vaccine Registration Form")

label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, sticky="e")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=1, column=0, sticky="e")
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

label_gender = tk.Label(root, text="Gender:")
label_gender.grid(row=2, column=0, sticky="e")
var_gender = tk.StringVar()
gender_male = tk.Radiobutton(root, text="Male", variable=var_gender, value="Male")
gender_male.grid(row=2, column=1, sticky="w")
gender_female = tk.Radiobutton(root, text="Female", variable=var_gender, value="Female")
gender_female.grid(row=2, column=1, sticky="e")

label_address = tk.Label(root, text="Address:")
label_address.grid(row=3, column=0, sticky="ne")
text_address = tk.Text(root, height=4, width=20)
text_address.grid(row=3, column=1)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=4, column=0, sticky="e")
entry_email = tk.Entry(root)
entry_email.grid(row=4, column=1)

label_contact = tk.Label(root, text="Contact No:")
label_contact.grid(row=5, column=0, sticky="e")
entry_contact = tk.Entry(root)
entry_contact.grid(row=5, column=1)

label_country = tk.Label(root, text="Country:")
label_country.grid(row=6, column=0, sticky="e")
entry_country = tk.Entry(root)
entry_country.grid(row=6, column=1)

label_state = tk.Label(root, text="State:")
label_state.grid(row=7, column=0, sticky="e")
entry_state = tk.Entry(root)
entry_state.grid(row=7, column=1)

label_diseases = tk.Label(root, text="Select if you are having any of the following disease:")
label_diseases.grid(row=8, column=0, columnspan=2)

cold_var = tk.BooleanVar()
cold_checkbox = tk.Checkbutton(root, text="Cold", variable=cold_var)
cold_checkbox.grid(row=9, column=0)

cough_var = tk.BooleanVar()
cough_checkbox = tk.Checkbutton(root, text="Cough", variable=cough_var)
cough_checkbox.grid(row=9, column=1)

fever_var = tk.BooleanVar()
fever_checkbox = tk.Checkbutton(root, text="Fever", variable=fever_var)
fever_checkbox.grid(row=10, column=0)

submit_button = tk.Button(root, text="Submit", command=register)
submit_button.grid(row=11, columnspan=2)

root.mainloop()
