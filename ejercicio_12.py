"""
Para realizar este ejercicio he utilizado dos clases donde en cada clase, se definen varios algoritmos, cada uno correspondiente a una operación.
En concreto, en la primera, se definen las estructuras de los datos, el saldo y las operaciones que se pueden realizar para una cuenta de depósito. 
Los algoritmos toman como datos de entrada el saldo inicial y la cantidad a retirar o a depositar, dependiendo de que operación se quiera llevar a cabo.
Si se quiere depositar dinero, simplemente el usuario tendrá que introducir la cantidad a depositar, y el algoritmno (el método depositar) devolverá
el saldo total que hay en la cuenta (inicial + el depositado). En cambio si se quiere retirar dinero, el algoritmo (correspondiente al método retirar)
toma como parametros el saldo inicial del usuario y la cantidad a retirar, verifica si ya hay un deposito en la cuenta (el saldo inical es mayor a 0).
Si la cantidad a retirar, es mayor al saldo de la cuenta, entonces deniega la operación (False), si se quiere retirar una cantidad a corde al saldo,
entonces la operación se realizará con exito. este último por tanto tiene dos posibles salidas en función de si se puede o no retirar la cantidad
pedida por el usuario.
"""

class Cuenta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad
        return self.saldo

    def retirar(self, cantidad):
        if self.saldo - cantidad >= 0:
            self.saldo -= cantidad
            return True  # La retirada fue validada
        else:
            return False  # No hay suficiente saldo para realizar la retirada 

"""
Esta segunda clase hereda de la clase padre "Cuenta", por ello, en el constructor, se reinicializa el atributo del saldo inicial
para que ul usuario no tenga que volver a introducirlo. Además la herencia me permite utilizar atributos (algoritmos) de la clase
padre, así como modificarlos. La clase funciona de la siguiente manera:
con el constructor, se reinicializa el atributo del saldo, y se crea un nuevo atributo, que guarda el límite del descubierto autorizado
al crear la cuenta. El algoritmo que contiene esta clase, es una modificación del algoritmo de retirada de deposito de la clase cuenta,
que toma como atributos la cantidad a retirar. La operación que realiza el algoritmo, es basicamente comprobar si se puede retirar la
cantidad deseada por el usuario, además de en función de la cantidad, como en la clase cuenta, teniendo en cuenta el limite descubierto
autorizado. Si la cantidad a retirar sobrepasa el saldo disponible y el descubierto autorizado, el retiro será denegado y el algoritmo
devuelve False. De lo contrario, el retiro se realiza con éxito y se actualiza el saldo de la cuenta.
"""

class CuentaConDescubierto(Cuenta):
    def __init__(self, saldo_inicial, descubierto_autorizado=0):
        super().__init__(saldo_inicial)
        self.descubierto_autorizado = descubierto_autorizado

    def retirar(self, cantidad):
        if self.saldo - cantidad >= -self.descubierto_autorizado:
            self.saldo -= cantidad
            return True  # La retirada fue exitosa
        else:
            return False  # No hay suficiente saldo para realizar la retirada dentro del descubierto autorizado
        
# Aquí se muestra un ejemplo de como funciona este algoritmo

# Crea una cuenta de depósito estándar con un saldo inicial de $1000
cuenta_estandar = Cuenta(1000)

# Deposita $500 en la cuenta estándar
saldo_tras_deposito = cuenta_estandar.depositar(500)
print("Saldo después del depósito en cuenta estándar:", saldo_tras_deposito)

# Intenta retirar $1500 de la cuenta estándar
resultado_retiro_estandar = cuenta_estandar.retirar(1500)
if resultado_retiro_estandar:
    print("Retiro realizado con éxito. Saldo actual en cuenta estándar:", cuenta_estandar.saldo)
else:
    print("No se puede retirar esa cantidad de la cuenta estándar. Saldo actual:", cuenta_estandar.saldo)

print("-----------------------------------------------")

# Crea una cuenta de depósito con descubierto autorizado con un saldo inicial de $1000 y límite de descubierto de $200
cuenta_con_descubierto = CuentaConDescubierto(1000, 200)

# Intenta retirar $1500 de la cuenta con descubierto autorizado
resultado_retiro_descubierto = cuenta_con_descubierto.retirar(1500)
if resultado_retiro_descubierto:
    print("Retiro exitoso. Saldo actual en cuenta con descubierto autorizado:", cuenta_con_descubierto.saldo)
else:
    print("No se puede retirar esa cantidad de la cuenta con descubierto autorizado. Saldo actual:", cuenta_con_descubierto.saldo)