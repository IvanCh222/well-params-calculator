import math
import sqlite3

import tkinter as tk
from tkinter import ttk

def execute_query(query):
    conn = sqlite3.connect("/Users/mac/Desktop/IAS.db")
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

def on_select(event):
    selected_well = event.widget.get(event.widget.curselection())
    load_and_calculate(selected_well)

def load_wells():
    query = "SELECT name_well FROM The_Well"
    wells = execute_query(query)
    return [well[0] for well in wells]

def fill_table(params):
    for item in tree.get_children():
        tree.delete(item)
    for row in params:
        tree.insert("", tk.END, text=row[0], values=row[1:])

def load_and_calculate(selected_well):
    query = f"SELECT * FROM PARAMETRS WHERE id_well IN (SELECT id_well FROM The_Well WHERE name_well = '{selected_well}')"
    params = execute_query(query)
    fill_table(params)

    # Заполнение параметров из последней выбранной скважины
    po, L, Py, Ty, Tz, Q, lk, D = [float(param) for param in params[-1][1:9]]
    print(po, L, Py, Ty, Tz, lk, D, Q)
    E = 2 * lk / D
    Lambda = 1 / (4 * (math.log10(7.41 / E)) ** 2)
    Tsr = (Ty + Tz) / 2
    Tkr = 125 * (po + 1)
    Pkr = 0.4903 * (10 - po)
    Tpr = Tsr / Tkr

    Ppr = Py / Pkr

    # Начальные значения для цикла
    Pz_n = 0

    # Условие выхода из цикла
    while True:
        # Вычисление Z, S и Pz

        Z = (0.4 * math.log10(Tpr) + 0.73) ** Ppr + 0.1 * Ppr
        S = 0.03415 * po * L / (Tsr * Z)
        Pz = math.sqrt((Py ** 2 * math.exp(2 * S) +
                            1.325 * 10 ** (-12) * (Z * Tsr * Q) ** 2 * Lambda *
                            (math.exp(2 * S) - 1) / D ** 5))
        Psr = (Py + Pz) / 2
        Ppr = Psr / Pkr

        # Проверка условия выхода из цикла
        if Pz_n is not None and abs(Pz - Pz_n) < 0.00000001:
            break

        # Обновление значения Pz для следующей итерации
        Pz_n = Pz
    differens_P = Pz-Py
    K =Q/differens_P
    print("Pz =", Pz, differens_P,K)



        # Здесь можно добавить любые дополнительные действия

root = tk.Tk()
root.title("Well Parameters")

well_list = load_wells()
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
well_listbox = tk.Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=well_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
well_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
for well in well_list:
    well_listbox.insert(tk.END, well)

well_listbox.bind("<<ListboxSelect>>", on_select)

tree = ttk.Treeview(root, height=10)
tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")  # Количество столбцов
tree.heading("#0", text="ID")
tree.column("#0", minwidth=0, width=50, stretch=tk.NO)  # Ширина столбца ID
tree.heading("1", text="Плотность")
tree.heading("2", text="Глубина")
tree.heading("3", text="Устьевое давление")
tree.heading("4", text="Устьевая температура")
tree.heading("5", text="Забойная температура")
tree.heading("6", text="Дебит")
tree.heading("7", text="Абсолютная шероховатость труб")
tree.heading("8", text="Внутренний диаметр труб")
tree.heading("9", text="Дата")
tree.pack(expand=True, fill="both")

root.mainloop()
