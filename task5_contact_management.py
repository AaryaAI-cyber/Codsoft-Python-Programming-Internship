# © 2026 Aarya Shinde | github.com/AaryaAI-cyber | All rights reserved
import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.title("CodSoft Task 5 - Contact Management by Aarya")
root.geometry("500x400")
root.configure(bg="#1e272e")
root.resizable(False, False)

contacts = []

listbox = tk.Listbox(root, font=("Arial", 14), bg="#2f3640", fg="#dcdde1", selectbackground="#353b48")
listbox.pack(fill=tk.BOTH, expand=True, pady=10, padx=20)

def refresh_list():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def add_contact():
    name = simpledialog.askstring("Name", "Enter Name:")
    if not name: return
    phone = simpledialog.askstring("Phone", "Enter Phone (10 digits):")
    if not phone or not phone.isdigit() or len(phone) != 10:
        messagebox.showerror("Error", "Invalid phone number!")
        return
    email = simpledialog.askstring("Email", "Enter Email:")
    if not email: return
    contacts.append({"name": name, "phone": phone, "email": email})
    refresh_list()

def search_contact():
    name = simpledialog.askstring("Search", "Enter Name to Search:")
    if not name: return
    found = [c for c in contacts if name.lower() in c['name'].lower()]
    if found:
        messagebox.showinfo("Found", "\n".join([f"{c['name']}: {c['phone']} ({c['email']})" for c in found]))
    else:
        messagebox.showinfo("Not Found", "No contact found!")

def update_contact():
    try:
        index = listbox.curselection()[0]
        contact = contacts[index]
        new_name = simpledialog.askstring("Update Name", "New Name:", initialvalue=contact['name'])
        if new_name: contact['name'] = new_name
        new_phone = simpledialog.askstring("Update Phone", "New Phone:", initialvalue=contact['phone'])
        if new_phone and len(new_phone) == 10 and new_phone.isdigit(): contact['phone'] = new_phone
        new_email = simpledialog.askstring("Update Email", "New Email:", initialvalue=contact['email'])
        if new_email: contact['email'] = new_email
        refresh_list()
    except:
        messagebox.showerror("Error", "Select a contact first!")

def delete_contact():
    try:
        index = listbox.curselection()[0]
        del contacts[index]
        refresh_list()
    except:
        messagebox.showerror("Error", "Select a contact first!")

frame = tk.Frame(root, bg="#1e272e")
frame.pack(pady=10)

tk.Button(frame, text="Add", font=("Arial", 14), bg="#27ae60", fg="white", command=add_contact).pack(side="left", padx=10)
tk.Button(frame, text="Search", font=("Arial", 14), bg="#2980b9", fg="white", command=search_contact).pack(side="left", padx=10)
tk.Button(frame, text="Update", font=("Arial", 14), bg="#f39c12", fg="white", command=update_contact).pack(side="left", padx=10)
tk.Button(frame, text="Delete", font=("Arial", 14), bg="#e74c3c", fg="white", command=delete_contact).pack(side="left", padx=10)

refresh_list()
root.mainloop()
