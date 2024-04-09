"""
Este script contiene 2 algoritmos, uno de ellos calcula la media aritmetica y el otro la media ponderada
"""
"""
Los parametros que quedan fuera de las funciones se definen de manera global, de esta forma los algoritmos
pueden tomar esos mismos parametros sin necesidad de definirlos de forma específica en cada función.
La primera función, es un algoritmo que calcula la media aritmetica de tres números cualesquiera
dados por el usuario (admite decimales). La entrada del algorítmo son esos tres numeros que introduce
el usuario, y la salida es la media aritmetica de esos tres numeros.
"""

n1 = float(input("Introduce el primer numero: "))
n2 = float(input("Introduce el segundo numero: "))
n3 = float(input("Introduce el tercer numero: "))

def calcular_media_aritmetica(n1 ,n2 ,n3):
    media_a = (n1 + n2 + n3)/3
    return media_a

# Muestra el resultado de la operación realizada por el algoritmo
print("la media aritmetica de los numeros introducidos es: ",calcular_media_aritmetica(n1, n2, n3))

"""
Esta segunda función realiza un calculo similar a la anterior, denominado media ponderada.
Toma la misma entrada que el otro algoritmo (tres numeros introducidos por el usuario) ademas
de tres parametros más, que son los tres coeficientes de ponderacion que introduzca el usuario.
Esta vez devuelve la media ponderada de los tres numeros introducidos, siendo esta
la salida del algoritmo 
"""
pond1 = float(input("Introduce el coeficiente de ponderación para el primer número: "))
pond2 = float(input("Introduce el coeficiente de ponderación para el segundo número: "))
pond3 = float(input("Introduce el coeficiente de ponderación para el tercer número: "))

def calcular_media_ponderada(n1, n2, n3, pond1, pond2, pond3):
    media_p = ((n1 * pond1) + (n2 * pond2) + (n3 * pond3)) / (pond1 + pond2 + pond3)
    return media_p

# Muestra el resultado de la operación realizada por el algoritmo 
print(f"la media ponderada de los tres numeros y sus coeficientes es:{calcular_media_ponderada(n1, n2, n3, pond1, pond2, pond3)}")