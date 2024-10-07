import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Трекер задач")
        self.tasks = load_tasks()

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Добавить задачу", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.tasks_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Удалить задачу", command=self.remove_task)
        self.delete_button.grid(row=2, column=0, padx=10, pady=10)

        self.complete_button = tk.Button(root, text="Отметить как выполнено", command=self.complete_task)
        self.complete_button.grid(row=2, column=1, padx=10, pady=10)

        self.display_tasks()

    def display_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            status = "✓" if task['completed'] else "✗"
            self.tasks_listbox.insert(tk.END, f"{i + 1}. [{status}] {task['title']}")

    def add_task(self):
        task_title = self.task_entry.get()
        if task_title:
            self.tasks.append({"title": task_title, "completed": False})
            save_tasks(self.tasks)
            self.display_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Ошибка", "Введите название задачи!")

    def remove_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            removed_task = self.tasks.pop(selected_task_index)
            save_tasks(self.tasks)
            self.display_tasks()
            messagebox.showinfo("Задача удалена", f"Задача '{removed_task['title']}' удалена.")
        except IndexError:
            messagebox.showwarning("Ошибка", "Выберите задачу для удаления.")

    def complete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks[selected_task_index]['completed'] = True
            save_tasks(self.tasks)
            self.display_tasks()
            messagebox.showinfo("Задача выполнена", f"Задача '{self.tasks[selected_task_index]['title']}' отмечена как выполненная.")
        except IndexError:
            messagebox.showwarning("Ошибка", "Выберите задачу для отметки как выполненную.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
