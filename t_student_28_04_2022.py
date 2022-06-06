import statistics as stat
import math
muestra = [3.2, 3, 2.8, 2.9, 3.1]
n=len(muestra)             # cantidad de datos
mean=stat.mean(muestra)    # media muestral
s=stat.stdev(muestra)      # desviacion estandar muestral

t=2.776                    # para un nivel de confianza al 95%

# usamos las formulas
ic1 = mean - t*(s/math.sqrt(n))     
ic2 = mean + t*(s/math.sqrt(n))
#print("Media: ", mean)
#print("Intervalo de confianza:", round(ic1, 2), round(ic2, 2))

#Ejercicio:
#Hacer una función que devuelva el intervalo de confianza.
#Calcular los intervalos de confianza a 80, 90, 95, 98 y 99% con la muestra:
#{3.33,3.15,2.91,3.05,2.75}

muestra1=[3.33,3.15,2.91,3.05,2.75]
ic=[80,90,95,98,99]
n1=len(muestra1)                     #cantidad de datos 
media=stat.mean(muestra1)           # media muestral
s1=stat.stdev(muestra1)             # desviacion estandar muestral
t1=[1.533,2.132,2.776,3.747,4.604]  # Para un nivel de confianza de 80, 90, 95, 98 y 99%
# usamos las formulas 
#ic11 = media - t*(s/math.sqrt(n1))     
#ic22 = media + t*(s/math.sqrt(n1))
ic11=[];ic22=[]
for i in range(0,n1):
    ic1_ = media - t1[i]*(s/math.sqrt(n1))     
    ic2_ = media + t1[i]*(s/math.sqrt(n1))
    ic11.append(ic1_)
    ic22.append(ic2_)
print("Media: ",media)    
for i in range(0,n1):
    print("Intervalo de confianza del",ic[i],"%",":" , round(ic11[i], 2),",", round(ic22[i], 2))    












