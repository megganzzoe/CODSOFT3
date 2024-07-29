import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Input error", "Please enter a positive number for the password length")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Input error", "Please enter a valid number for the password length")
window = tk.Tk()
window.title('Password Generator')
window.geometry('400x300')
tk.Label(window, text='Password Generator', font=('Arial', 25)).pack(pady=20)
tk.Label(window, text='Specify password length:', font=('Arial', 15)).pack(pady=5)
entry_length = tk.Entry(window)
entry_length.pack(pady=5)
tk.Label(window, text='Generated Password:', font=('Arial', 15)).pack(pady=5)
entry_password = tk.Entry(window, font=('Arial', 12))
entry_password.pack(pady=5)
tk.Button(window, text='Generate Password', bg='green', fg='white', font=('Arial', 14), command=generate_password).pack(pady=20)
window.mainloop()