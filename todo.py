import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        del tasks[task_index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def mark_as_completed():
    try:
        task_index = listbox.curselection()[0]
        tasks[task_index] = tasks[task_index] + " (Completed)"
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")

root = tk.Tk()
root.title("To-Do List")

# Styling the GUI
root.geometry("400x400")
root.configure(bg="#f0f0f0")

tasks = []

task_entry = tk.Entry(root, width=35, borderwidth=2)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#4CAF50", fg="white", borderwidth=0)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#FF5733", fg="white", borderwidth=0)
delete_button.pack(pady=5)

completed_button = tk.Button(root, text="Mark as Completed", command=mark_as_completed, bg="#3498DB", fg="white", borderwidth=0)
completed_button.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=10, bg="#f0f0f0", borderwidth=0)
listbox.pack(pady=15)

root.mainloop()
