import tkinter as tk
from tkinter import messagebox, scrolledtext
from pathlib import Path
import os

# ---------------- BACKEND FUNCTIONS ---------------- #

def list_files():
    file_list.delete(0, tk.END)
    p = Path('')
    for file in p.iterdir():
        file_list.insert(tk.END, file.name)


def create_file():
    name = entry_name.get()
    content = text_area.get("1.0", tk.END)

    if not name:
        messagebox.showerror("Error", "Enter file name")
        return

    p = Path(name)
    if p.exists():
        messagebox.showwarning("Warning", "File already exists!")
    else:
        with open(name, "w") as f:
            f.write(content)
        messagebox.showinfo("Success", "File Created!")
        list_files()


def read_file():
    name = entry_name.get()
    p = Path(name)

    if p.exists():
        with open(name, "r") as f:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, f.read())
    else:
        messagebox.showerror("Error", "File Not Found!")


def update_file():
    name = entry_name.get()
    content = text_area.get("1.0", tk.END)
    p = Path(name)

    if p.exists():
        with open(name, "w") as f:
            f.write(content)
        messagebox.showinfo("Updated", "File Updated!")
    else:
        messagebox.showerror("Error", "File Not Found!")


def delete_file():
    name = entry_name.get()
    p = Path(name)

    if p.exists():
        os.remove(p)
        messagebox.showinfo("Deleted", "File Deleted!")
        text_area.delete("1.0", tk.END)
        list_files()
    else:
        messagebox.showerror("Error", "File Not Found!")

# ---------------- UI DESIGN ---------------- #

root = tk.Tk()
root.title("CRUD File Manager")
root.geometry("700x500")
root.config(bg="#1e1e1e")

tk.Label(root, text="File Manager", font=("Arial", 18, "bold"), fg="white", bg="#1e1e1e").pack(pady=10)

entry_name = tk.Entry(root, width=40, font=("Arial", 12))
entry_name.pack(pady=5)

text_area = scrolledtext.ScrolledText(root, width=70, height=12)
text_area.pack(pady=10)

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack()

tk.Button(button_frame, text="Create", width=10, command=create_file, bg="#4CAF50").grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Read", width=10, command=read_file, bg="#2196F3").grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Update", width=10, command=update_file, bg="#FFC107").grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Delete", width=10, command=delete_file, bg="#F44336").grid(row=0, column=3, padx=5)

tk.Label(root, text="Files in Directory", fg="white", bg="#1e1e1e").pack(pady=5)

file_list = tk.Listbox(root, width=60)
file_list.pack()

list_files()

root.mainloop()