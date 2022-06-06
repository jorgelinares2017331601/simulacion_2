# en este programa aproximaremos el numero pi 
# se hara una simulacion del experimento de Buffon
import random
import numpy as np
import matplotlib.pyplot as plt
limite=100
xa1=[]
ya1=[]
at=[5,2,3,4,2]#alfileres que tocan la linea
x1=[];x2=[];x3=[];x4=[];x5=[];x6=[];x7=[];x8=[];x9=[]
y=[]
for i in range(0,limite):
    ys=random.random();y.append(ys)
    xa=0.5;xb=0.1;xc=0.2;xd=0.3;xe=0.4;xf=0.6;xg=0.7;xh=0.8;xi=0.9
    x1.append(xa);x2.append(xb);x3.append(xc);x4.append(xd);x5.append(xe)
    x6.append(xf);x7.append(xg);x8.append(xh);x9.append(xi);
    xa2=random.random()
    ya2=random.random()
    xa1.append(xa2)
    ya1.append(ya2)
    if ys==ya2:
        at.append(ys)
#Realizamos el calculo de pi
print(at)
suma=len(at)
pi=2*(limite/63)
print(f"El valor de pi es {pi}")
#Empezamos a graficar los puntos aleatorios y las lineas rectas
plt.plot(x1,y,color="red",linewidth="1") #linea 1
plt.plot(x2,y,color="red",linewidth="1") #linea 2
plt.plot(x3,y,color="red",linewidth="1") #linea 3
plt.plot(x4,y,color="red",linewidth="1") #linea 4
plt.plot(x5,y,color="red",linewidth="1") #linea 5
plt.plot(x6,y,color="red",linewidth="1") #linea 6
plt.plot(x7,y,color="red",linewidth="1") #linea 7
plt.plot(x8,y,color="red",linewidth="1") #linea 8
plt.plot(x9,y,color="red",linewidth="1") #linea 9
plt.grid(which="major")
plt.xlabel("X")
plt.ylabel("Y")    
plt.title("Simulación del experimento de Buffon")    
plt.scatter(xa1,ya1, color="blue", marker   =".")     
plt.show()












#fig = plt.figure(1, figsize=(8, 8)) 
#plt.axis("equal")                             
#plt.grid(which="major")                        
#plt.plot(xgrafica,ygrafica, color="red" , ) 
#
#plt.scatter(xcuadrado,ycuadrado, color="green"  , marker   =".") 
#
#














