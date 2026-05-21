# © 2026 Aarya Shinde | github.com/AaryaAI-cyber | All rights reserved
import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("CodSoft - To Do List (Task 1)")
root.geometry("500x650")
root.configure(bg="#1e272e")

tasks = []

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, f" {task}")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please type something!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        tasks.pop(index)
    except:
        messagebox.showwarning("No Selection", "Select a task to delete!")

def mark_done():
    try:
        index = listbox.curselection()[0]
        task_text = tasks[index]
        listbox.delete(index)
        listbox.insert(index, f" {task_text} (Done)")
    except:
        messagebox.showwarning("No Selection", "Select a task first!")

# Title
tk.Label(root, text="MY TO-DO LIST", font=("Helvetica", 24, "bold"), fg="#00d2ff", bg="#1e272e").pack(pady=20)

# Entry box
entry = tk.Entry(root, width=40, font=("Arial", 14), bd=5, relief="flat")
entry.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#1e272e")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Task", width=12, bg="#00d2ff", fg="white", font=("bold"), command=add_task).grid(row=0, column=0, padx=8)
tk.Button(btn_frame, text="Mark Done", width=12, bg="#2ecc71", fg="white", font=("bold"), command=mark_done).grid(row=0, column=1, padx=8)
tk.Button(btn_frame, text="Delete", width=12, bg="#e74c3c", fg="white", font=("bold"), command=delete_task).grid(row=0, column=2, padx=8)

# Listbox + Scrollbar
frame = tk.Frame(root)
frame.pack(pady=20)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, width=50, height=15, font=("Arial", 12), bg="#2f3640", fg="white", selectbackground="#00d2ff", yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT)
scrollbar.config(command=listbox.yview)

root.mainloop()
