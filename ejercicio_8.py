"""
Esta función corresponde al primer apartado del ejercicio 8.
Calcula el precio con todos los impuestos incluidos (TII) para un precio sin impuestos
y un porcentaje de IVA dado por un input que introduzca el usuario (admite números decimales)
"""

def calcular_precio_con_impuestos():

    precio_sin_impuestos = float(input("Introduce el precio sin impuestos: "))
    porcentaje_iva = float(input("Introduce el porcentaje de IVA: "))
    
    impuestos = precio_sin_impuestos * (porcentaje_iva / 100)
    precio_con_impuestos = precio_sin_impuestos + impuestos
    return precio_con_impuestos

"""
Esta función corresponde al segundo apartado del ejercicio 8.
Calcula el importe de los intereses generados por un capital invertido a un interés dado
durante un tiempo, en meses (todos estos datos los proporciona el usuario). Admite valores decimales
"""

def calcular_intereses():
   
    capital = float(input("Introduce el capital invertido: "))
    tasa_interes = float(input("Introduce la tasa de interés anual: "))
    tiempo_meses = int(input("Introduce el tiempo de inversión en meses: "))
    
    tasa_mensual = tasa_interes / 12 / 100  # Tasa de interés mensual
    intereses = capital * tasa_mensual * tiempo_meses
    return intereses

# LLama a las funciones y muestra los resultados calculados por las funciones.
precio_con_impuestos = calcular_precio_con_impuestos()
print("El precio total con impuestos incluidos es:", precio_con_impuestos)

intereses_generados = calcular_intereses()
print("Los intereses generados son:", intereses_generados)