import sqlite3
import tkinter as tk
from tkinter import ttk

def fetch_data():
    # Подключение к базе данных
    conn = sqlite3.connect('/Users/mac/Desktop/всякое/sqlite/bd.db')
    cursor = conn.cursor()

    # Выполнение SQL-запроса
    cursor.execute('SELECT * FROM Users')

    # Получение результатов
    rows = cursor.fetchall()

    # Закрытие соединения с базой данных
    conn.close()

    # Очистка предыдущих данных в Treeview
    for row in tree.get_children():
        tree.delete(row)

    # Вставка данных в Treeview
    for row in rows:
        tree.insert("", "end", values=row)

def process_data():
    # Получение всех данных из столбца "Колонка3"
    conn = sqlite3.connect('имя_вашей_базы_данных.db')
    cursor = conn.cursor()
    cursor.execute('SELECT Колонка3 FROM имя_вашей_таблицы')  # Замените на реальные названия
    values = [row[0] for row in cursor.fetchall()]
    conn.close()
    # Подсчет суммы значений
    total_sum = sum(values)
    # Отображение суммы в окне программы
    result_label.config(text=f"Сумма значений в столбце 'Колонка3': {total_sum}")

# Создание главного окна
root = tk.Tk()
root.title("Отображение данных из SQLite")

# Создание Treeview
columns = ("ID", "Name", "Age")
tree = ttk.Treeview(root, columns=columns, show='headings')

# Настройка заголовков столбцов
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

# Кнопка для загрузки данных
load_button = tk.Button(root, text="Загрузить данные", command=fetch_data)
load_button.pack(pady=10)

# Размещение Treeview на форме
tree.pack()

# Запуск главного цикла событий
root.mainloop()
