import tkinter as tk
from tkinter import messagebox


class Student:
    def __init__(self, roll_no, name, age, grade):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.grade = grade


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, roll_no, name, age, grade):
        student = Student(roll_no, name, age, grade)
        self.students.append(student)
        messagebox.showinfo("Success", "Student added successfully.")

    def display_students(self):
        if not self.students:
            messagebox.showinfo("Information", "No students in the system.")
        else:
            student_info = "Student Details:\n"
            for student in self.students:
                student_info += f"Roll No: {student.roll_no}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}\n"
            messagebox.showinfo("Student Details", student_info)

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                messagebox.showinfo("Student Found",
                                    f"Student found - Roll No: {student.roll_no}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
                return
        messagebox.showinfo("Information", "Student not found.")

    def delete_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                messagebox.showinfo("Success", "Student deleted successfully.")
                return
        messagebox.showinfo("Information", "Student not found.")

    def update_student(self, roll_no, name=None, age=None, grade=None):
        for student in self.students:
            if student.roll_no == roll_no:
                if name:
                    student.name = name
                if age:
                    student.age = age
                if grade:
                    student.grade = grade
                messagebox.showinfo("Success", "Student details updated successfully.")
                return
        messagebox.showinfo("Information", "Student not found.")


def add_student_window():
    add_window = tk.Toplevel(root)
    add_window.title("Add Student")

    roll_label = tk.Label(add_window, text="Roll No:")
    roll_label.grid(row=0, column=0)
    roll_entry = tk.Entry(add_window)
    roll_entry.grid(row=0, column=1)

    name_label = tk.Label(add_window, text="Name:")
    name_label.grid(row=1, column=0)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=1, column=1)

    age_label = tk.Label(add_window, text="Age:")
    age_label.grid(row=2, column=0)
    age_entry = tk.Entry(add_window)
    age_entry.grid(row=2, column=1)

    grade_label = tk.Label(add_window, text="Grade:")
    grade_label.grid(row=3, column=0)
    grade_entry = tk.Entry(add_window)
    grade_entry.grid(row=3, column=1)

    add_button = tk.Button(add_window, text="Add Student",
                           command=lambda: add_student(roll_entry.get(), name_entry.get(), age_entry.get(),
                                                       grade_entry.get()))
    add_button.grid(row=4, columnspan=2, pady=10)


def add_student(roll_no, name, age, grade):
    if roll_no and name and age and grade:
        sms.add_student(roll_no, name, age, grade)
    else:
        messagebox.showerror("Error", "All fields are required.")


def display_students():
    sms.display_students()


def search_student_window():
    search_window = tk.Toplevel(root)
    search_window.title("Search Student")

    roll_label = tk.Label(search_window, text="Roll No:")
    roll_label.grid(row=0, column=0)
    roll_entry = tk.Entry(search_window)
    roll_entry.grid(row=0, column=1)

    search_button = tk.Button(search_window, text="Search", command=lambda: search_student(roll_entry.get()))
    search_button.grid(row=1, columnspan=2, pady=10)


def search_student(roll_no):
    if roll_no:
        sms.search_student(roll_no)
    else:
        messagebox.showerror("Error", "Please enter Roll No.")


def delete_student_window():
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Student")

    roll_label = tk.Label(delete_window, text="Roll No:")
    roll_label.grid(row=0, column=0)
    roll_entry = tk.Entry(delete_window)
    roll_entry.grid(row=0, column=1)

    delete_button = tk.Button(delete_window, text="Delete", command=lambda: delete_student(roll_entry.get()))
    delete_button.grid(row=1, columnspan=2, pady=10)


def delete_student(roll_no):
    if roll_no:
        sms.delete_student(roll_no)
    else:
        messagebox.showerror("Error", "Please enter Roll No.")


def update_student_window():
    update_window = tk.Toplevel(root)
    update_window.title("Update Student")

    roll_label = tk.Label(update_window, text="Roll No:")
    roll_label.grid(row=0, column=0)
    roll_entry = tk.Entry(update_window)
    roll_entry.grid(row=0, column=1)

    name_label = tk.Label(update_window, text="Name (leave blank to skip):")
    name_label.grid(row=1, column=0)
    name_entry = tk.Entry(update_window)
    name_entry.grid(row=1, column=1)

    age_label = tk.Label(update_window, text="Age (leave blank to skip):")
    age_label.grid(row=2, column=0)
    age_entry = tk.Entry(update_window)
    age_entry.grid(row=2, column=1)

    grade_label = tk.Label(update_window, text="Grade (leave blank to skip):")
    grade_label.grid(row=3, column=0)
    grade_entry = tk.Entry(update_window)
    grade_entry.grid(row=3, column=1)

    update_button = tk.Button(update_window, text="Update",
                              command=lambda: update_student(roll_entry.get(), name_entry.get(), age_entry.get(),
                                                             grade_entry.get()))
    update_button.grid(row=4, columnspan=2, pady=10)


def update_student(roll_no, name, age, grade):
    if roll_no:
        sms.update_student(roll_no, name, age, grade)
    else:
        messagebox.showerror("Error", "Please enter Roll No.")


def exit_app():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


root = tk.Tk()
root.title("Student Management System")

sms = StudentManagementSystem()

add_button = tk.Button(root, text="Add Student", command=add_student_window)
add_button.pack(pady=10)

display_button = tk.Button(root, text="Display Students", command=display_students)
display_button.pack(pady=10)

search_button = tk.Button(root, text="Search Student", command=search_student_window)
search_button.pack(pady=10)

delete_button = tk.Button(root, text="Delete Student", command=delete_student_window)
delete_button.pack(pady=10)

update_button = tk.Button(root, text="Update Student", command=update_student_window)
update_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=10)

root.mainloop()
