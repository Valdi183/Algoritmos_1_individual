"""
Esta función corresponde al primer apartado del ejercicio 8.
Es un algoritmo que calcula el precio con todos los impuestos incluidos (TII) para un precio sin impuestos
y un porcentaje de IVA dado por un input que introduzca el usuario, es decir, las entradas del algorítmo
(admiten números decimales). El algoritmo devuelve el precio con los impuestos añadidos.
"""

def calcular_precio_con_impuestos():

    precio_sin_impuestos = float(input("Introduce el precio sin impuestos: "))
    porcentaje_iva = float(input("Introduce el porcentaje de IVA: "))
    
    impuestos = precio_sin_impuestos * (porcentaje_iva / 100)
    precio_con_impuestos = precio_sin_impuestos + impuestos
    return precio_con_impuestos

"""
Esta función corresponde al segundo apartado del ejercicio 8.
Calcula el importe de los intereses generados con un algorítmo,por un capital invertido a un interés dado
durante un tiempo, en meses. Todos estos datos los proporciona el usuario ya que son las entradas del
algoritmo (admiten valores decimales). El algoritmo devuelve los intereses calculados.
"""

def calcular_intereses():
   
    capital = float(input("Introduce el capital invertido: "))
    tasa_interes = float(input("Introduce la tasa de interés anual: "))
    tiempo_meses = int(input("Introduce el tiempo de inversión en meses: "))
    
    tasa_mensual = tasa_interes / 12 / 100  # Tasa de interés mensual
    intereses = capital * tasa_mensual * tiempo_meses
    return intereses

# LLama a las funciones (algoritmos) y muestra los resultados indicando a que corresponde cada output (salida del algoritmo).
precio_con_impuestos = calcular_precio_con_impuestos()
print("El precio total con impuestos incluidos es:", precio_con_impuestos)

intereses_generados = calcular_intereses()
print("Los intereses generados son:", intereses_generados)