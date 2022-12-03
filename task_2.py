# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

import matplotlib.pyplot as plt
import numpy as np
from random import randint as rdt

fig = plt.figure()
fig2 = plt.figure()
ax = fig.add_subplot()
ax3 = fig.add_subplot()
ax2 = fig2.add_subplot()


S = [(rdt(100,301), rdt(3_000_000, 20_000_001)) for _ in range(15)]

x = [i for i in range(len(S))]
y = [S[i][1]/S[i][0] for i in range(len(S))]
y.sort()

y2 = [i for i in y if i < 50_000]
x2 = [y.index(i) for i in y2]

y3 = [50_000 for _ in range(0, 15)]

ax.set_title('Стоимости квадратного метра каждого дома')
ax.set_xlabel("Номер дома")
ax.set_ylabel("Стоймость м2")
ax.set_xticks(np.arange(0, 15, step=1))
ax.set_yticks(np.arange(0, 200_000, step=10_000))

ax.bar(x, y)
ax3.plot(x,y3, color="red")


ax2.set_title('Дома стоимости м2 < 50 000 ')
ax2.set_xlabel("Номер дома")
ax2.set_ylabel("Стоймость м2")
ax2.set_yticks(np.arange(0, 55_000, step=5_000))
ax2.set_xticks(np.arange(0, len(x2), step=1))
ax2.bar(x2, y2)
fig.show()
fig2.show()

