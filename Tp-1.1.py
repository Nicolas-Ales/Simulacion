#Como ejercicio tenemos que hacer una ruleta y hacer las graficas
#1- fr/n frecuencia relativa #cantidad de veces que SALIO el numero / cantidad total de muestras
#2- vp/n valor promedio de las tiradas
#3- vd/n valor del desvio       np.std(datos, 0) # Desviación típica de cada columna
#4- vv/n valor de la varianza
import numpy as np
import pandas as pd
import statistics as st


def mensaje():
    print ("Bienvenido a la ruleta!!")


def ruleta(n):
    return np.random.randint(0, 36, n)


def AnalizarDatos(datos):
    a = pd.value_counts(datos) #encontras la frecuencia absoluta de cada numero
    dataframe = pd.DataFrame(a, columns=["FrAbs"])
    print(dataframe)
    print("media aritmetica", st.mean(datos)) #mostrar media aritmetica
    print("desviacion estandar", st.pstdev(datos,st.mean(datos)))
    print("varianza", st.variance(datos))



def main():
    mensaje()
    d = ruleta(int(input("Ingrese la cantidad de muestras que desea: ")))
    #print(d)
    AnalizarDatos(d)


main()
