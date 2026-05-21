# © 2026 Aarya Shinde | github.com/AaryaAI-cyber | All rights reserved
import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import string

root = tk.Tk()
root.title("CodSoft Task 3 - Password Generator by Aarya")
root.geometry("400x300")
root.configure(bg="#1e272e")
root.resizable(False, False)

tk.Label(root, text="Password Length:", font=("Arial", 14), bg="#1e272e", fg="#dcdde1").pack(pady=10)
length_var = tk.IntVar(value=12)
length_slider = tk.Scale(root, from_=8, to_=32, orient="horizontal", variable=length_var, bg="#2f3640", fg="#dcdde1", troughcolor="#353b48")
length_slider.pack()

include_upper = tk.BooleanVar(value=True)
include_lower = tk.BooleanVar(value=True)
include_digits = tk.BooleanVar(value=True)
include_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Uppercase Letters", variable=include_upper, bg="#1e272e", fg="#dcdde1", selectcolor="#353b48").pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Lowercase Letters", variable=include_lower, bg="#1e272e", fg="#dcdde1", selectcolor="#353b48").pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Digits", variable=include_digits, bg="#1e272e", fg="#dcdde1", selectcolor="#353b48").pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Symbols", variable=include_symbols, bg="#1e272e", fg="#dcdde1", selectcolor="#353b48").pack(anchor="w", padx=20)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 16), bg="#2f3640", fg="#dcdde1", justify="center", state="readonly")
password_entry.pack(pady=10)

def generate_password():
    length = length_var.get()
    if length < 8:
        messagebox.showerror("Error", "Length must be at least 8!")
        return
    
    chars = ""
    if include_upper.get():
        chars += string.ascii_uppercase
    if include_lower.get():
        chars += string.ascii_lowercase
    if include_digits.get():
        chars += string.digits
    if include_symbols.get():
        chars += string.punctuation
    
    if not chars:
        messagebox.showerror("Error", "Select at least one option!")
        return
    
    password = "".join(random.choice(chars) for _ in range(length))
    password_var.set(password)
    password_entry.config(state="normal")
    password_entry.selection_range(0, tk.END)

def copy_password():
    if password_var.get():
        root.clipboard_clear()
        root.clipboard_append(password_var.get())
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password generated!")

tk.Button(root, text="Generate", font=("Arial", 14), bg="#27ae60", fg="white", command=generate_password).pack(pady=5)
tk.Button(root, text="Copy to Clipboard", font=("Arial", 14), bg="#2980b9", fg="white", command=copy_password).pack(pady=5)

root.mainloop()
