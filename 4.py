import math
po=0.57
L=1840
Py=17.9
Ty=312
Tz=321.2
lk=0.00004
D=0.112
Q=349

E=2*lk/D
print(E)

Lambda = 1 / (4 * (math.log10( 7.41/E)) ** 2)
print(Lambda)
Tsr=(Ty+Tz)/2
print(Tsr)

Tkr= 125 * (po + 1)
print(Tkr)
Pkr=0.4903*(10-po)
print(Pkr)
Tpr=Tsr/Tkr
Ppr=Py/Pkr

Z = (0.4 * math.log10(Tpr) + 0.73) ** Ppr + 0.1 * Ppr

print("Z =", Z)

S = 0.03415 * po * L / (Tsr * Z)

print("S =", S)

Pz = math.sqrt((Py ** 2 * math.exp(2 * S) +
                1.325 * 10 ** (-12) * (Z * Tsr * Q) ** 2 *Lambda  *
                (math.exp(2 * S) - 1) / D ** 5))
print(Pz)

Psr=(Py+Pz)/2
Ppr=Psr/Pkr
print(Ppr)