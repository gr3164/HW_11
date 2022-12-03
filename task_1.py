# Задача 1. Постройте график функции
# 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.

import matplotlib.pyplot as plt
import numpy as np
   
x = [x for x in range(-6,6)]
y = [5 * x[i] * x[i] + 10 * x[i] - 30 for i in range(len(x))]
 
plt.plot(x,y, marker="o")   
plt.xticks(np.arange(-5, 5, step=1))   
plt.title("График функции f(x)=5*x*x+10*x-30") 
plt.xlabel('Ось x')    
plt.ylabel('Ось y') 
plt.show()   

print('Значение функции отрицательно при х < -1')