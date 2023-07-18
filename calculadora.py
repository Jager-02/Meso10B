#Calculadora basica de 2 numeros

num1 = 0
num2 = 0

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

#Funciones para hacer las operaciones aritméticas
def suma(numero1, numero2):
    suma = numero1 + numero2
    return suma

def resta(numero1, numero2):
    resta = numero1 - numero2
    return resta

def multi(numero1, numero2):
    multi = numero1 * numero2
    return multi

def division(numero1, numero2):
    division = numero1 / numero2
    return division

#Menu principal
opcion = 0

while(opcion != 5):
    print("\nPor favor, elija una opción:\n"
      "1. Suma \n"
      "2. Resta \n"
      "3. Multiplicación \n"
      "4. División \n"
      "5. Salir \n")

    opcion = int(input("Digite la opción a elegir: \n"))

    #Condicional para elegir opción
    if(opcion==1):
        resultadoSuma = suma(num1,num2)
        print("La suma es: ", resultadoSuma)
    elif(opcion==2):
        resultadoResta = resta(num1,num2)
        print("La resta es: ", resultadoResta)
    elif(opcion==3):
        resultadoMulti = multi(num1,num2)
        print("La multiplicación es: ", resultadoMulti)
    elif(opcion==4):
        resultadoDivision = division(num1,num2)
        print("La división es: ", resultadoDivision)
    elif(opcion==5):
        print("Gracias por usar la calculadora")
        break
    else:
        print("Opción no válida")    