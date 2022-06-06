# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 22:09:42 2022

@author: 80157
"""

import numpy as np;
import matplotlib.pyplot as plt
import random

n=1000
a=1
b=0.4
l1=[];l2=[]
l3=[];l4=[]
cuenta=[];aciertos=0
def f(x):
    return (b/a)*np.sqrt((a**2)-(x**2))
for i in range(0,n):
    x1=random.random()
    y1=random.random()
    if y1<(b/a)*np.sqrt((a**2)-(x1**2)):
        l1.append(x1)
        l2.append(y1)
        aciertos+=1
        cuenta.append(aciertos)
    else:
        l3.append(x1)
        l4.append(y1)

print("Se utilizan numeros aleatorios que siguen una distribucion uniforme (0,1)")   
print("Aciertos que caen dentro de la funcion:  ",len(cuenta))
print("Aciertos que caen fuera de la funcion:  ",np.abs(n-len(cuenta)))
print("Total de aciertos:  ",n)        
x=np.linspace(0,1,1000)
v=[0,1,0,1]
plt.plot(x,f(x),color="red" )
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Función de un cuarto de elipse")
plt.scatter(l1,l2, color="blue"  , marker   =".")
plt.scatter(l3,l4, color="green"  , marker   =".")
plt.axis(v);plt.grid()


