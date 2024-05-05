import tkinter as tk
from tkinter import ttk
import sqlite3

def execute_query(query):
    conn = sqlite3.connect("/Users/mac/Desktop/IAS.db")
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows


# Функции для открытия новой формы и возврата в меню
def open_new_form1():
    root.withdraw()  # Скрыть главное окно (меню)
    new_window = tk.Toplevel()
    new_window.title("Состояние скважины")
    new_window.geometry("800x600")  # Увеличенный размер формы
    new_window.resizable(False, False)  # Запрет на изменение размера
    label = tk.Label(new_window, text="Это новая форма 1", font=("Arial", 20), fg="#333333")  # Установка шрифта и цвета текста
    label.pack(pady=20)

    # Создание виджета Treeview
    tree = ttk.Treeview(new_window, height=10, )
    tree["columns"] = ("1", "2", "3","4")  # Количество столбцов
    tree.heading("#0", text="ID")
    tree.column("#0", minwidth=0, width=50, stretch=tk.NO)  # Ширина столбца ID

    # Установка заголовков для столбцов
    tree.heading("1", text="Дебит")
    tree.heading("2", text="Депрессия")
    tree.heading("3", text="Забойное давление")
    tree.heading("4", text="Дата")

    # Подключение к базе данных и выполнение запроса
    query = "SELECT * FROM PARAMETRS"
    result = execute_query(query)

    # Заполнение таблицы данными из базы
    for row in result:
        tree.insert("", tk.END, text=row[0], values=row[1:])

    # Размещение таблицы на форме
    tree.pack(expand=False, fill="x")

    # Функция для вывода последней записи дебита в Label
    def show_last_debit():
        query = "SELECT Debit FROM PARAMETRS ORDER BY ROWID DESC LIMIT 1"
        last_debit = execute_query(query)[0][0]
        last_debit_label.config(text=f"Последний дебит: {last_debit}")

    # Кнопка для вызова функции вывода последней записи дебита
    last_debit_button = tk.Button(new_window, text="Показать последний дебит", command=show_last_debit)
    last_debit_button.pack(side="left", padx=20, pady=20)

    # Label для отображения последнего дебита
    last_debit_label = tk.Label(new_window, text="", font=("Arial", 12))
    last_debit_label.pack(side="left", padx=10, pady=10)


    back_button = tk.Button(new_window, text="Назад", command=lambda: return_to_menu(root, new_window), bg="#ff9999", font=("Arial", 16))  # Увеличенный размер кнопки и цвет
    back_button.pack(side="bottom",pady=20, anchor="s")



def open_new_form2():
    root.withdraw()  # Скрыть главное окно (меню)
    new_window = tk.Toplevel()
    new_window.title("Новая форма 2")
    new_window.geometry("600x400")  # Увеличенный размер формы
    new_window.resizable(False, False)  # Запрет на изменение размера
    label = tk.Label(new_window, text="Это новая форма 2", font=("Arial", 20), fg="#333333")  # Установка шрифта и цвета текста
    label.pack(pady=20)
    back_button = tk.Button(new_window, text="Назад", command=lambda: return_to_menu(root, new_window), bg="#ffd966", font=("Arial", 16))  # Увеличенный размер кнопки и цвет
    back_button.pack(pady=20)



def open_new_form3():
    root.withdraw()  # Скрыть главное окно (меню)
    new_window = tk.Toplevel()
    new_window.title("Новая форма 3")
    new_window.geometry("600x400")  # Увеличенный размер формы
    new_window.resizable(False, False)  # Запрет на изменение размера
    label = tk.Label(new_window, text="Это новая форма 3", font=("Arial", 20), fg="#333333")  # Установка шрифта и цвета текста
    label.pack(pady=20)
    back_button = tk.Button(new_window, text="Назад", command=lambda: return_to_menu(root, new_window), bg="#c2f0fc", font=("Arial", 16))  # Увеличенный размер кнопки и цвет
    back_button.pack(pady=20)



def open_new_form4():
    root.withdraw()  # Скрыть главное окно (меню)
    new_window = tk.Toplevel()
    new_window.title("Новая форма 4")
    new_window.geometry("600x400")  # Увеличенный размер формы
    new_window.resizable(False, False)  # Запрет на изменение размера
    label = tk.Label(new_window, text="Это новая форма 4", font=("Arial", 20), fg="#333333")  # Установка шрифта и цвета текста
    label.pack(pady=20)
    back_button = tk.Button(new_window, text="Назад", command=lambda: return_to_menu(root, new_window), bg="#ff9999", font=("Arial", 16))  # Увеличенный размер кнопки и цвет
    back_button.pack(pady=20)

def return_to_menu(menu, window):
    window.destroy()  # Закрыть текущее окно
    menu.deiconify()  # Показать главное окно (меню)

# Создание главного окна (меню)
root = tk.Tk()
root.title("Меню")

# Установка размера и зафиксирование окна
root.geometry("800x500")  # Увеличенные размеры
root.resizable(False, False)  # Запрет на изменение размера

# Создание фона и настройка цвета
background_color = "#f2f2f2"
root.configure(bg=background_color)

# Создание рамки для кнопок вверху
button_frame_top = tk.Frame(root, bg=background_color)
button_frame_top.pack(pady=50)

# Создание кнопок с цветом фона вверху
button1 = tk.Button(button_frame_top, text="Состояние скважины", command=open_new_form1, bg="#ff9999", font=("Arial", 18), width=20, height=2)  # Увеличенный размер кнопки и цвет
button2 = tk.Button(button_frame_top, text="Открыть форму 2", command=open_new_form2, bg="#ffd966", font=("Arial", 18), width=20, height=2)  # Увеличенный размер кнопки и цвет

# Размещение кнопок вверху
button1.grid(row=0, column=0, padx=20)  # Увеличенный отступ
button2.grid(row=0, column=1, padx=20)  # Увеличенный отступ

# Создание рамки для кнопок внизу
button_frame_bottom = tk.Frame(root, bg=background_color)
button_frame_bottom.pack(pady=50)

# Создание кнопок с цветом фона внизу
button3 = tk.Button(button_frame_bottom, text="Открыть форму 3", command=open_new_form3, bg="#c2f0fc", font=("Arial", 18), width=20, height=2)  # Увеличенный размер кнопки и цвет
button4 = tk.Button(button_frame_bottom, text="Открыть форму 4", command=open_new_form4, bg="#ff9999", font=("Arial", 18), width=20, height=2)  # Увеличенный размер кнопки и цвет

# Размещение кнопок внизу
button3.grid(row=0, column=0, padx=20)  # Увеличенный отступ
button4.grid(row=0, column=1, padx=20)  # Увеличенный отступ

# Запуск главного цикла событий
root.mainloop()
