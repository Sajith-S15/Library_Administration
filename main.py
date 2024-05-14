import tkinter as tk
from tkinter import messagebox

class LibraryManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.master.geometry("400x400")
        self.master.config(bg='#708090')

        self.books = []
        self.lend_list = []
        self.admins = []
        self.students = []

        self.current_user = None
        self.current_frame = None
        self.frames = {}

        self.create_login_screen()

    def create_login_screen(self):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = tk.Frame(self.master, bg='#708090')
        self.current_frame.pack(padx=10, pady=10)

        self.frames['login'] = self.current_frame

        self.login_label = tk.Label(self.current_frame, text="Login", font=("Helvetica", 16), bg='#708090', fg='white')
        self.login_label.pack(pady=10)

        self.username_label = tk.Label(self.current_frame, text="Username", font=("Helvetica", 12), bg='#708090', fg='white')
        self.username_label.pack()

        self.username_entry = tk.Entry(self.current_frame, font=("Helvetica", 12))
        self.username_entry.pack(pady=10)

        self.password_label = tk.Label(self.current_frame, text="Password", font=("Helvetica", 12), bg='#708090', fg='white')
        self.password_label.pack()

        self.password_entry = tk.Entry(self.current_frame, font=("Helvetica", 12), show="*")
        self.password_entry.pack(pady=10)

        self.admin_button = tk.Button(self.current_frame, text="Admin Login", command=self.admin_login, font=("Helvetica", 12))
        self.admin_button.pack(pady=5)

        self.student_button = tk.Button(self.current_frame, text="Student Login", command=self.student_login, font=("Helvetica", 12))
        self.student_button.pack(pady=5)

        self.register_button = tk.Button(self.current_frame, text="Register", command=self.show_register_screen, font=("Helvetica", 12))
        self.register_button.pack(pady=5)

    def show_register_screen(self):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = tk.Frame(self.master, bg='#708090')
        self.current_frame.pack(padx=10, pady=10)

        self.frames['register'] = self.current_frame

        self.register_label = tk.Label(self.current_frame, text="Register", font=("Helvetica", 16), bg='#708090', fg='white')
        self.register_label.pack(pady=10)

        self.username_label = tk.Label(self.current_frame, text="Username", font=("Helvetica", 12), bg='#708090', fg='white')
        self.username_label.pack()

        self.username_entry = tk.Entry(self.current_frame, font=("Helvetica", 12))
        self.username_entry.pack(pady=10)

        self.password_label = tk.Label(self.current_frame, text="Password", font=("Helvetica", 12), bg='#708090', fg='white')
        self.password_label.pack()

        self.password_entry = tk.Entry(self.current_frame, font=("Helvetica", 12), show="*")
        self.password_entry.pack(pady=10)

        self.admin_register_button = tk.Button(self.current_frame, text="Register as Admin", command=self.register_admin, font=("Helvetica", 12))
        self.admin_register_button.pack(pady=5)

        self.student_register_button = tk.Button(self.current_frame, text="Register as Student", command=self.register_student, font=("Helvetica", 12))
        self.student_register_button.pack(pady=5)

        self.back_button = tk.Button(self.current_frame, text="Back to Login", command=self.create_login_screen, font=("Helvetica", 12))
        self.back_button.pack(pady=5)

    def register_admin(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.admins.append((username, password))
        messagebox.showinfo("Success", "Admin registration successful")

    def register_student(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.students.append((username, password))
        messagebox.showinfo("Success", "Student registration successful")

    def admin_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if (username, password) in self.admins:
            self.current_user = (username, password)
            self.create_admin_section()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def student_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if (username, password) in self.students:
            self.current_user = (username, password)
            self.create_student_section()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def create_admin_section(self):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = tk.Frame(self.master, bg='#708090')
        self.current_frame.pack(padx=10, pady=10)

        self.frames['admin'] = self.current_frame

        self.add_book_button = tk.Button(self.current_frame, text="Add Book", command=self.add_book, font=("Helvetica", 12))
        self.add_book_button.pack(pady=5)

        self.remove_book_button = tk.Button(self.current_frame, text="Remove Book", command=self.remove_book, font=("Helvetica", 12))
        self.remove_book_button.pack(pady=5)

        self.view_books_button = tk.Button(self.current_frame, text="View Books", command=self.view_books, font=("Helvetica", 12))
        self.view_books_button.pack(pady=5)

        self.logout_button = tk.Button(self.current_frame, text="Logout", command=self.logout, font=("Helvetica", 12))
        self.logout_button.pack(pady=5)

    def create_student_section(self):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = tk.Frame(self.master, bg='#708090')
        self.current_frame.pack(padx=10, pady=10)

        self.frames['student'] = self.current_frame

        self.view_books_button = tk.Button(self.current_frame, text="View Available Books", command=self.view_books, font=("Helvetica", 12))
        self.view_books_button.pack(pady=5)

        self.issue_book_button = tk.Button(self.current_frame, text="Issue Book", command=self.issue_book, font=("Helvetica", 12))
        self.issue_book_button.pack(pady=5)

        self.return_book_button = tk.Button(self.current_frame, text="Return Book", command=self.return_book, font=("Helvetica", 12))
        self.return_book_button.pack(pady=5)

        self.view_issued_books_button = tk.Button(self.current_frame, text="View Issued Books", command=self.view_issued_books, font=("Helvetica", 12))
        self.view_issued_books_button.pack(pady=5)

        self.logout_button = tk.Button(self.current_frame, text="Logout", command=self.logout, font=("Helvetica", 12))
        self.logout_button.pack(pady=5)

    def add_book(self):
        if self.current_user in self.admins:
            if self.current_frame:
                self.current_frame.pack_forget()
            self.current_frame = tk.Frame(self.master, bg='#708090')
            self.current_frame.pack(padx=10, pady=10)

            self.frames['add_book'] = self.current_frame

            self.book_label = tk.Label(self.current_frame, text="Book Name", font=("Helvetica", 12), bg='#708090', fg='white')
            self.book_label.pack()

            self.book_entry = tk.Entry(self.current_frame, font=("Helvetica", 12))
            self.book_entry.pack(pady=10)

            self.submit_button = tk.Button(self.current_frame, text="Submit", command=self.submit_book, font=("Helvetica", 12))
            self.submit_button.pack(pady=5)
        else:
            messagebox.showerror("Error", "Only admin can add books")

    def submit_book(self):
        book = self.book_entry.get()
        if book:
            self.books.append(book)
            messagebox.showinfo("Success", "Book added successfully")
            self.current_frame.pack_forget()
            self.create_admin_section()
        else:
            messagebox.showerror("Error", "Please enter a book name")

    def remove_book(self):
        if self.current_user in self.admins:
            book = self.get_book_name()
            if book in self.books:
                self.books.remove(book)
                messagebox.showinfo("Success", "Book removed successfully")
            else:
                messagebox.showerror("Error", "Book not found")
        else:
            messagebox.showerror("Error", "Only admin can remove books")

    def view_books(self):
        if self.books:
            message = "\n".join(self.books)
            messagebox.showinfo("Available Books", message)
        else:
            messagebox.showinfo("Available Books", "No books available")

    def issue_book(self):
        if self.current_user in self.students:
            book = self.get_book_name()
            if book in self.books:
                self.lend_list.append(book)
                messagebox.showinfo("Success", "Book issued successfully")
            else:
                messagebox.showerror("Error", "Book not found")
        else:
            messagebox.showerror("Error", "Only student can issue books")

    def return_book(self):
        if self.current_user in self.students:
            book = self.get_book_name()
            if book in self.lend_list:
                self.lend_list.remove(book)
                messagebox.showinfo("Success", "Book returned successfully")
            else:
                messagebox.showerror("Error", "Book not found in lend list")
        else:
            messagebox.showerror("Error", "Only student can return books")

    def view_issued_books(self):
        if self.lend_list:
            message = "\n".join(self.lend_list)
            messagebox.showinfo("Issued Books", message)
        else:
            messagebox.showinfo("Issued Books", "No books issued yet")

    def logout(self):
        if self.current_frame:
            self.current_frame.pack_forget()
            self.create_login_screen()

    def get_book_name(self):
        book_name = self.book_entry.get()
        return book_name

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagement(root)
    root.mainloop()
