import tkinter as tk
'''Imports Tkinter module'''

# Button click handler
def press(v):
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)
    
def backspace():
    current = entry.get()
    if current:
        entry.delete(len(current)-1, tk.END)
def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Expression")

# Main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Entry widget (display)
entry = tk.Entry(
    root,
    font=("Times New Roman", 20),
    bg="#2d2d2d",
    fg="white",
    bd=0,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)

# Button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Create buttons dynamically
r, c = 1, 0

for b in buttons:
    cmd = calc if b == "=" else lambda x=b: press(x)

    tk.Button(
        root,
        text=b,
        command=cmd,
        font=("Calibri", 14),
        width=5,
        height=2,
        bg="#ff9500" if b in "+-*/" else "#3a3a3a",
        fg="white",
        bd=0
    ).grid(row=r, column=c, padx=6, pady=6)

    c += 1
    if c == 4:
        r += 1
        c = 0

# Clear button
tk.Button(
    root,
    text="C",
    command=clear,
    font=("Calibri", 14),
    bg="#f6ea07",
    fg="black",
    bd=5,
    width=22,
    height=2
).grid(row=r, column=0, columnspan=3, pady=8)
#backspace button
tk.Button(
    root,
    text="B",
    command=backspace,
    font=("Calibri", 14),
    bg="#41e321",
    fg="black",
    bd=5,
    width=14,
    height=2
).grid(row=r, column=2, columnspan=2, pady=8)
root.mainloop()
