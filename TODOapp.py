#TO DO LIST GUI APPLICATION

import tkinter as tk
from tkinter import simpledialog, messagebox

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("500x350")

# Set the background color of the main window
root.configure(bg='powder blue')

# Title label
title_label = tk.Label(root, text="To-Do List Application ", font=( 'aria' ,20, 'bold' ), fg='steel blue', bg='white')
title_label.pack(pady=20)

# Initialize an empty list to store tasks
tasks = []

# Function to add a new task
def add_task():
    new_task = simpledialog.askstring("Add Task", "Enter New Task:",parent=root)
    if new_task:
        tasks.append(new_task)
        messagebox.showinfo("Success", f"Task '{new_task}' Added Successfully!")


# Function to update the task list
def update_task():
    if not tasks:
        messagebox.showwarning("No Tasks", "No tasks available to update.")
        return

    old_task = simpledialog.askstring("Update Task", "Enter the task to be updated:",parent=root)
    if old_task in tasks:
        new_task = simpledialog.askstring("Update Task", "Enter the New Task:",parent=root)
        index = tasks.index(old_task)
        tasks[index] = new_task
        messagebox.showinfo("Success",f"Task {new_task} Updated Successfully!")
    else:
        messagebox.showerror("Error", "Task {old_task} not found!")

# Function to delete a task
def delete_task():
    if not tasks:
        messagebox.showwarning("No Tasks", "No tasks available to delete.")
        return

    task_to_delete = simpledialog.askstring("Delete Task", "Enter the task to be deleted:")
    if task_to_delete in tasks:
        tasks.remove(task_to_delete)
        messagebox.showinfo("Success", f"Task {task_to_delete} Deleted Successfully!")
    else:
        messagebox.showerror("Error", f"Task {task_to_delete} not found!")

# Function to view task list
def view_tasks():
    if not tasks:
        messagebox.showinfo("No Tasks", "No tasks to display!")
    else:
        tasks_string = "\n".join(tasks)
        messagebox.showinfo("Your Tasks", tasks_string)

# Function to exit the application
def exit_app():
    root.destroy()

# Buttons
Add_button = tk.Button(root, text="Add Task", command=add_task, font=( 'aria' ,9, 'bold' ), fg='black', bg='white', pady=5, width=20, bd=2)
Add_button.pack(pady=10)

Update_button = tk.Button(root, text="Update Task", command=update_task, font=( 'aria' ,9, 'bold' ), fg='black', bg='white', pady=5, width=20, bd=2)
Update_button.pack(pady=10)

Delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=( 'aria' ,9, 'bold' ), fg='black', bg='white', pady=5, width=20, bd=2)
Delete_button.pack(pady=10)

View_button = tk.Button(root, text="View Tasks", command=view_tasks, font=( 'aria' ,9, 'bold' ),fg='black', bg='white', pady=5, width=20, bd=2)
View_button.pack(pady=10)

Exit_button = tk.Button(root, text="Exit", command=exit_app, font=( 'aria' ,9, 'bold' ), fg='black', bg='white', pady=5, width=20, bd=2)
Exit_button.pack(pady=10)

# Run the application
root.mainloop()
