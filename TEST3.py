import tkinter as tk
import sqlite3

# Функция для открытия новой формы и возврата в меню
def open_new_form(form_number):
    root.withdraw()  # Скрыть главное окно (меню)
    new_window = tk.Toplevel()
    new_window.title(f"Новая форма {form_number}")
    new_window.geometry("600x400")  # Увеличенный размер формы
    new_window.resizable(False, False)  # Запрет на изменение размера
    label = tk.Label(new_window, text=f"Это новая форма {form_number}", font=("Arial", 20), fg="#333333")  # Установка шрифта и цвета текста
    label.pack(pady=20)
    back_button = tk.Button(new_window, text="Назад", command=lambda: return_to_menu(root, new_window), bg="#ff9999", font=("Arial", 16))  # Увеличенный размер кнопки и цвет
    back_button.pack(pady=20)

def return_to_menu(menu, window):
    window.destroy()  # Закрыть текущее окно
    menu.deiconify()  # Показать главное окно (меню)

 # Функция для вывода данных из таблицы PARAMS
def display_params():
    conn = sqlite3.connect("/Users/mac/Desktop/всякое/sqlite/IAS.db")  # Замените "your_database.db" на путь к вашей базе данных SQLite
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PARAMETRS")
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        print(row)  # Замените вывод на нужную вам обработку данных, например, вывод на новую форму

# Создание главного окна (меню)
root = tk.Tk()
root.title("Меню")

# Установка размера и зафиксирование окна
root.geometry("800x500")  # Увеличенные размеры
root.resizable(False, False)  # Запрет на изменение размера

# Создание фона и настройка цвета
background_color = "#f2f2f2"
root.configure(bg=background_color)

# Создание рамки для кнопок
button_frame = tk.Frame(root, bg=background_color)
button_frame.pack(pady=50)

# Создание кнопок с цветом фона
button1 = tk.Button(button_frame, text="Вывести данные из таблицы PARAMS", command=display_params, bg='#FF9999', font=("Arial", 18), width=30, height=2)  # Увеличенный размер кнопки и цвет
button2 = tk.Button(button_frame, text="Открыть форму 2", command=lambda: open_new_form(2), bg='#ffd966', font=("Arial", 18), width=20, height=2)  # Увеличенный размер кнопки и цвет
button3 = tk.Button(button_frame, text="Открыть форму 3", command=lambda: open_new_form(3), bg='#CCf0CC', font=("Arial", 18), width=20, height=2)  # Увеличенный размер кнопки и цвет
button4 = tk.Button(button_frame, text="Открыть форму 4", command=lambda: open_new_form(4), bg="#ff9999", font=("Arial", 18), width=20, height=2)  # Увеличенный размер кнопки и цвет

# Размещение кнопок в рамке
button1.grid(row=0, column=0, padx=20, pady=10)  # Увеличенные отступы
button2.grid(row=0, column=1, padx=20, pady=10)  # Увеличенные отступы
button3.grid(row=1, column=0, padx=20, pady=10)  # Увеличенные отступы
button4.grid(row=1, column=1, padx=20, pady=10)  # Увеличенные отступы

# Запуск главного цикла событий
root.mainloop()
