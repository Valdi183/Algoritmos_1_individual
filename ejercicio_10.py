"""
La  función, es un sencillo algoritmo que calcula el area de un triángulo, tomando como entrada
los parametros del lado y altura del triángulo (admite valores decimales). El algoritmo devuelve el area calculada.
(teniendo en cuenta que los parametros se introducen en metros, devuelve el resultado en m^2)
"""

# Se definen los parametros (inputs) que utiliza el algoritmo.
lado = float(input("Introduce la medida del lado del triángulo: "))
altura = float(input("Introduce la altura relativa al lado dado: "))

def area_triangulo(lado, altura):
    area = (lado * altura) / 2
    return area

# Muetsra el resultado de la operación realizada por el algoritmo
print("El área del triángulo es:", area_triangulo(lado, altura),"dada en m^2") 

"""
Para calcular la altura de un triángulo rectangulo, podemos utizar el mismo algoritmo, teniendo en cuenta
que la altura del triángulo, ahora corresponde con uno de los lados (un cateto) y el otro lado seria el otro cateto.
"""