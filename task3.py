import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    length = int(length_var.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)
root = tk.Tk()
root.title(" codsoft Password Generator")
root.geometry("400x300")
tk.Label(root, text="Password Length:").pack(pady=10)
length_var = tk.StringVar(value="12")
tk.Entry(root, textvariable=length_var).pack()
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=20)
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, state='readonly').pack(pady=10)
root.mainloop()
