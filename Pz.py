import math



po = 0.61
L = 4850
Py = 46.5
Ty = 350
Tz = 374.5
lk = 0.000045
D = 0.062
Q = 172

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

    print(Ppr, Tpr)
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


print("Pz =", Pz)


