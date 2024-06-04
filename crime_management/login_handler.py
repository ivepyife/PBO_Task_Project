from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector


class LoginWindow:
    def __init__(self, root):
        self.login_successful = False
        self.root = root
        self.root.title("Login")
        self.root.geometry('480x480')

        # Frame untuk login form
        frame = Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Title label
        self.label_title = Label(
            root, text="Login", font=('Roboto', 20, 'bold'))
        self.label_title.place(relx=0.5, rely=0.3, anchor=CENTER, y=-50)

        img_logo = Image.open('./images/police_logo.jpg')
        img_logo = img_logo.resize((60, 60), Image.ADAPTIVE)
        self.photo_logo = ImageTk.PhotoImage(img_logo)
        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=210, y=5, width=60, height=60)

        self.label_username = Label(
            frame, text="Username:", font=('Roboto', 11, 'bold'))
        self.label_password = Label(
            frame, text="Password:", font=('Roboto', 11, 'bold'))
        self.entry_username = Entry(frame, width=30)
        self.entry_password = Entry(frame, show="*", width=30)

        self.label_username.grid(row=0, column=0, pady=10)
        self.entry_username.grid(row=0, column=1, pady=10)
        self.label_password.grid(row=1, column=0, pady=10)
        self.entry_password.grid(row=1, column=1, pady=10)

        self.display_users_button = Button(frame, text='Lihat Pengguna', font=(
            'Roboto', 13, 'bold'), width=14, bg='green', fg='white', command=self.display_users)
        self.display_users_button.grid(row=4, columnspan=2, pady=10)

        self.login_button = Button(frame,  text='Login', font=(
            'Roboto', 13, 'bold'), width=14, bg='blue', fg='white', command=self.login)
        self.login_button.grid(row=2, columnspan=2, pady=20)

        self.register_button = Button(
            frame,  text='Register', font=(
                'Roboto', 13, 'bold'), width=14, bg='blue', fg='white', command=self.open_registration_window)
        self.register_button.grid(row=3, columnspan=2, pady=10)

        self.root.bind('<Return>', self.login)

        self.conn = mysql.connector.connect(
            host='147.139.195.118', port='3306', username='admin', password='SOK1PSTIC', database='management')
        self.cursor = self.conn.cursor()

    def login(self, event=''):
        username = self.entry_username.get()
        password = self.entry_password.get()

        self.cursor.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = self.cursor.fetchone()

        if user:
            self.login_successful = True
            self.root.destroy()

        else:
            messagebox.showerror(
                "Login", "Username atau password salah", messagebox.OK)

    def open_registration_window(self):
        self.registration_window = Toplevel(self.root)
        self.registration_window.title("Register")
        self.registration_window.geometry('400x300')

        frame = Frame(self.registration_window)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        label_new_username = Label(
            frame, text="New Username:", font=('Roboto', 11, 'bold'))
        label_new_password = Label(
            frame, text="New Password:", font=('Roboto', 11, 'bold'))
        self.entry_new_username = Entry(frame, width=30)
        self.entry_new_password = Entry(frame, width=30)

        label_new_username.grid(row=0, column=0, pady=10)
        self.entry_new_username.grid(row=0, column=1, pady=10)
        label_new_password.grid(row=1, column=0, pady=10)
        self.entry_new_password.grid(row=1, column=1, pady=10)

        self.register_button = Button(
            frame,  text='Register', font=(
                'Roboto', 13, 'bold'), width=14, bg='blue', fg='white', command=self.register)
        self.register_button.grid(row=2, columnspan=2, pady=20)

    def register(self):
        new_username = self.entry_new_username.get()
        new_password = self.entry_new_password.get()

        self.cursor.execute(
            "SELECT * FROM users WHERE username=%s", (new_username,))
        existing_user = self.cursor.fetchone()

        if existing_user:
            messagebox.showerror(
                "Registrasi Gagal", "Username sudah ada, coba gunakan username yang lain")
        else:
            self.cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)", (new_username, new_password))
            self.conn.commit()
            messagebox.showinfo(
                "Registrasi Berhasil", "Registrasi Berhasil, Silahkan Login!!")
            self.registration_window.destroy()

    def display_users(self):
        display_window = Toplevel(self.root)
        display_window.title("Registered Users")
        display_window.geometry('400x300')

        frame = Frame(display_window)
        frame.pack(fill=BOTH, expand=True)

        tree = ttk.Treeview(frame, columns=(
            'Username', 'Password'), show='headings')
        tree.heading('Username', text='Username')
        tree.heading('Password', text='Password')
        tree.column('Username', width=100)
        tree.column('Password', width=100)

        scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        tree.pack(fill=BOTH, expand=True)

        self.cursor.execute("SELECT username, password FROM users")
        for user in self.cursor.fetchall():
            tree.insert('', END, values=user)

        display_window.mainloop()
