# © 2026 Aarya Shinde | github.com/AaryaAI-cyber | All rights reserved
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("CodSoft Task 2 - Calculator by Aarya")
root.geometry("320x460")
root.configure(bg="#1e272e")
root.resizable(False, False)

display = tk.Entry(root, font=("Helvetica", 24), bg="#2f3640", fg="#dcdde1", bd=10, relief="flat", justify="right")
display.pack(fill=tk.X, padx=15, pady=20, ipady=15)

buttons = [
    ['C', '±', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=', '']
]

frame = tk.Frame(root, bg="#1e272e")
frame.pack(pady=10)

def click(val):
    if val == "=":
        try:
            result = str(eval(display.get()))
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            messagebox.showerror("Error", "Invalid Input!")
            display.delete(0, tk.END)
    elif val == "C":
        display.delete(0, tk.END)
    elif val == "±":
        if display.get() and display.get()[0] == "-":
            display.delete(0)
        else:
            display.insert(0, "-")
    elif val == "%":
        try:
            display.insert(0, str(eval(display.get()) / 100))
        except:
            messagebox.showerror("Error", "Invalid!")
    else:
        display.insert(tk.END, val)

for i, row in enumerate(buttons):
    for j, txt in enumerate(row):
        if txt == "": continue
        btn_color = "#e74c3c" if txt in "C" else "#f39c12" if txt in "=±%" else "#353b48"
        btn = tk.Button(frame, text=txt, font=("Arial", 20, "bold"), fg="white", bg=btn_color,
                        command=lambda x=txt: click(x))
        btn.grid(row=i, column=j, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

    frame.grid_rowconfigure(i, weight=1)
    for col in range(4):
        frame.grid_columnconfigure(col, weight=1)

root.mainloop()
