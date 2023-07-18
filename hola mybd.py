#Variables y Tipos de datos
x = 45 # int
nombre = "Belarmino es bueno" # str
Booleano = False # bool
pi = 3.1416 # float
nombres = ["Fatima", "Kenia", "Herbert"] # list


# Funciones

def suma(a, b):
    resultado = a + b
    return resultado

def resta(a, b):
    resultado = a - b
    return resultado

def multiplicacion(a, b):
    resultado = a * b
    return resultado

def division(a, b):
    resultado = a / b
    return resultado

#Ejemplos

suma1 = suma(15,20)
print("La suma es:", suma1)

resta1 = resta(35, 15)
print("La resta es:", resta1)

multiplicacion1 = multiplicacion(5, 5)
print("La multiplicacion es:", multiplicacion1)

division1 = division(10, 2)
print("La division es:", division1)

#Ejercicio en clase
# 5 puntos extra

suma2 = suma(suma1, resta1)
suma3 = suma(multiplicacion1, division1)
sumaFinal = suma(suma2, suma3)
print("La suma final es:", sumaFinal)


