import tkinter as tk

def add_task(): # добавить задачу в очередь
    new_entry = entry.get()
    if new_entry:
        task_list1.insert(tk.END, new_entry)

def task_list1(): # взять задачу в работу
    selection = task_list1.curselection()
    task_list2.insert(tk.END, task_list1.get(selection))
    task_list1.delete(selection)
def task_list2(): # перенести задачу в выполненные
    selection = task_list1.curselection()
    task_list3.insert(tk.END, task_list1.get(selection))
    task_list1.delete(selection)
def task_list3(): # удалить задачу
    selection = task_list1.curselection()
    task_list1.delete(selection)

def task_work1(): # вернуть в очередь
    selection = task_list2.curselection()
    task_list1.insert(tk.END, task_list2.get(selection))
    task_list2.delete(selection)
def task_work2(): # перенести задачу в выполненные
    selection = task_list2.curselection()
    task_list3.insert(tk.END, task_list2.get(selection))
    task_list2.delete(selection)
def task_work3(): # удалить задачу
    selection = task_list2.curselection()
    task_list2.delete(selection)

def task_end1(): # вернуть в очередь
    selection = task_list3.curselection()
    task_list1.insert(tk.END, task_list3.get(selection))
    task_list3.delete(selection)
def task_end2(): # вернуть в работу
    selection = task_list3.curselection()
    task_list2.insert(tk.END, task_list3.get(selection))
    task_list3.delete(selection)
def task_end3(): # удалить задачу
    selection = task_list3.curselection()
    task_list3.delete(selection)

# Большая рамка
root = tk.Tk()
root.title("Управление задачами")
root.geometry("1300x700")
root.configure(bg="SlateGray1", pady = 10, padx = 10)

# Рамка ввода новой задачи
task_enter = tk.Frame(root)
task_enter.configure(bg = "light cyan", width = 500, height = 400, pady = 10, padx = 10)
task_enter.grid(row=0, column=1, padx = 10, pady = 10)
# Описание
label = tk.Label(task_enter, pady = 5, text = "Опишите новую задачу в поле ввода и нажмите синюю кнопку ВВОД НОВОЙ ЗАДАЧИ")
label.configure(width = 75)
label.grid(row=1, column=1, padx = 10, pady = 10)
# Поле ввода
entry = tk.Entry(task_enter, width = 80)
entry.grid(row=2, column=1, padx = 10, pady = 10)
# Кнопка "ВВОД ЗАДАЧИ"
add_task_button = tk.Button(task_enter,
    text = "ВВОД НОВОЙ ЗАДАЧИ",
    fg = "black", bg = "SteelBlue1",
    command=add_task)
add_task_button.grid(row=3, column=1, padx = 10, pady = 10)
# Заголовок "Работа с задачами"
work = tk.Label(root, text = "Работа с задачами", bg = "SlateGray1", pady = 5)
work.grid(row=3, column=1, padx = 10, pady = 10)
# Три колонки
task_1 = tk.Label(root, text = "Новые задачи", width=30, padx = 10, pady = 5)
task_1.grid(row=4, column=0, padx = 10, pady = 10)
task_2 = tk.Label(root, text = "Задачи в работе", width=30, padx = 10, pady = 5)
task_2.grid(row=4, column=1, padx = 10, pady = 10)
task_3 = tk.Label(root, text = "Выполненные задачи", width=30, padx = 10, pady = 5)
task_3.grid(row=4, column=2, padx = 10, pady = 10)

# Кнопки обработки задач левые
task_list_button1 = tk.Button(root,
    text = "ВЗЯТЬ В РАБОТУ",
    fg = "black", bg = "LightGreen",
    command=task_list1)
task_list_button1.grid(row=5, column=0, padx = 10, pady = 10)
task_list_button2 = tk.Button(root,
    text = "ЗАДАЧА ВЫПОЛНЕНА",
    fg = "black", bg = "LightGreen",
    command=task_list2)
task_list_button2.grid(row=6, column=0, padx = 10, pady = 10)
task_list_button3 = tk.Button(root,
    text = "УДАЛИТЬ ЗАДАЧУ",
    fg = "black", bg = "LightPink",
    command=task_list3)
task_list_button3.grid(row=7, column=0, padx = 10, pady = 10)

# Кнопки обработки задач центральные
task_work_button1 = tk.Button(root,
    text = "ВЕРНУТЬ В ОЧЕРЕДЬ",
    fg = "black", bg = "LightGreen",
    command=task_work1)
task_work_button1.grid(row=5, column=1, padx = 10, pady = 10)
task_work_button2 = tk.Button(root,
    text = "ЗАДАЧА ВЫПОЛНЕНА",
    fg = "black", bg = "LightGreen",
    command=task_work2)
task_work_button2.grid(row=6, column=1, padx = 10, pady = 10)
task_work_button3 = tk.Button(root,
    text = "УДАЛИТЬ ЗАДАЧУ",
    fg = "black", bg = "LightPink",
    command=task_work3)
task_work_button3.grid(row=7, column=1, padx = 10, pady = 10)

# Кнопки обработки задач правые
task_end_button1 = tk.Button(root,
    text = "ВЕРНУТЬ В ОЧЕРЕДЬ",
    fg = "black", bg = "LightGreen",
    command=task_end1)
task_end_button1.grid(row=5, column=2, padx = 10, pady = 10)
task_end_button2 = tk.Button(root,
    text = "ВЕРНУТЬ В РАБОТУ",
    fg = "black", bg = "LightGreen",
    command=task_end2)
task_end_button2.grid(row=6, column=2, padx = 10, pady = 10)
task_end_button3 = tk.Button(root,
    text = "УДАЛИТЬ ЗАДАЧУ",
    fg = "black", bg = "LightPink",
    command=task_end3)
task_end_button3.grid(row=7, column=2, padx = 10, pady = 10)

# Список новых задач
task_list1 = tk.Listbox(root, bg="light cyan", width=40, height=15)
task_list1.grid(row=8, column=0, padx=10, pady=10)
# Список задач в работе
task_list2 = tk.Listbox(root, bg="light cyan", width=40, height=15)
task_list2.grid(row=8, column=1, padx=10, pady=10)
# Список выполненных задач
task_list3 = tk.Listbox(root, bg="light cyan", width=40, height=15)
task_list3.grid(row=8, column=2, padx=10, pady=10)

root.mainloop()