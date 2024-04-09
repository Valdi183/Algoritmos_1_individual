
"""
La función definida a continuación es ya un algoritmo relativamente más complejo, quue realiza unos calculos en función
de ciertos requisitos pedidos en el ejercicio, funciona de la siguiente manera:
Primero, toma como entradas los parametros que introduzca el usuario, en este caso el salario mensual bruto, que puede ser
decimal, y el numero de horas extra trabajadas, que tiene que ser entero. El algoritmo calcula el importe a pagar por las
horas extra, cuyo importe concreto se hará en función de el número de horas (ordinarias y extras), y de las horas totales, 
es decir, las horas ordinarias más las horas extra. Para ello, se utilizan condicionales, que en función del numero de horas, 
aplica unoscalculos u otros según las normas administrativas.
"""

# Se definen los atributos como inputs, que además actuan como inputs del algoritmo
salario_mensual_bruto = float(input("Introduce el salario mensual bruto del empleado: "))
horas_extra_trabajadas = int(input("Introduce la cantidad de horas extra trabajadas en el mes: "))

def calcular_horas_extra(salario_mensual_bruto, horas_extra_trabajadas):
    horas_normales_por_semana = 35
    semanas_por_mes = 52 / 12
    horas_normales_por_mes = horas_normales_por_semana * semanas_por_mes
    salario_por_hora = salario_mensual_bruto / horas_normales_por_mes

    # Calcula el importe de las horas extra según los requisitos
    importe_horas_extra = 0
    if horas_extra_trabajadas > 0:
        if horas_extra_trabajadas <= 7:  # Hasta la hora 35 incluida
            importe_horas_extra += salario_por_hora * 1.25 * horas_extra_trabajadas
        elif horas_extra_trabajadas <= 8:  # Entre la hora 36 y 43 incluida
            importe_horas_extra += salario_por_hora * 1.25 * 7
            importe_horas_extra += salario_por_hora * 1.5 * (horas_extra_trabajadas - 7)
        else:  # A partir de la hora 44
            importe_horas_extra += salario_por_hora * 1.25 * 7
            importe_horas_extra += salario_por_hora * 1.5 * (8 - 7)
            importe_horas_extra += salario_por_hora * 1.5 * 1.5 * (horas_extra_trabajadas - 8)

    return importe_horas_extra

# Asigana una variable a la función, para facilitar su uso (al llamarla) y muestra el resultado de los calculos del algoritmo
importe_horas_extra = calcular_horas_extra(salario_mensual_bruto, horas_extra_trabajadas)
print("El importe a pagar por las horas extra es:", importe_horas_extra)