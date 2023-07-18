num1 = 0 
num2 = 0 
num3 = 0
num4 = 0 
num5 = 0

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

#ingresa la opcion

opcion = 0

while(opcion != 7): #Menu
    print("\nPor favor, elija una opcion:\n"
        "1 Circulo \n"
        "2 Triangulo rectangulo \n"
        "3 Rectangulo \n"
        "4 Cuadrado \n"
        "5 Trapecio \n"
        "6 Paralelogramo \n"
        "7 salir \n")
    opcion = int(input("Digite la opcion a elegir: "))

#las condiciones de la operaciones

    if(opcion==1):
        num1 = int(input("ingrese el radio del circulo: "))
        resultadoCir = multi(num1,num1)
        num3 = resultadoCir
        num2 = 3.14
        resultadoCirculo = multi(num3,num2)
        print("El area del circulo es: ", resultadoCirculo)
    elif(opcion==2):
        num1 = int(input("Ingrese el primer cateto: "))
        num2 = int(input("Ingrese el segundo cateto: "))
        ResultadoTraingulorec = multi(num1,num2)
        num3 = ResultadoTraingulorec
        resultadoTotal = division(num3,2)
        print("El area del Traingulo rectangulo es: ", resultadoTotal)
    elif(opcion==3):
        num1 = int(input("Ingrese el largo: "))
        num2 = int(input("Ingrese el ancho: "))
        resultadoRectangulo = multi(num1,num2)
        print("El area del Rectangulo es: ", resultadoRectangulo)
    elif(opcion==4):
        num1 = int(input("Ingrese un lado: "))
        resultadoCuadrado = multi(num1,num1)
        print("El area del rectangulo es: ", resultadoCuadrado)
    elif(opcion==5):
        num1 = int(input("Ingrese la base: "))
        num2 = int(input("Ingrese la base pequeña: "))
        num3 = int(input("Ingrese la altura: "))
        resultadoSuma = suma(num1,num2)
        num4 = resultadoSuma
        resultadoDiv = division(num4,2)
        num5 = resultadoDiv
        resultadoTotal = multi(num5,num3)
        print("El area del Trapecio es: ", resultadoTotal)
    elif(opcion==6):
        num1 = int(input("Ingrese el largo: "))
        num2 = int(input("Ingrese el ancho: "))
        resultadoparalelo = multi(num1,num2)
        print("El area del Paralelogramo es: ", resultadoparalelo)
    elif(opcion==7):
        print("gracias por usar la calculadora de areas")
        break
    else:
        print("La opcion no es valida")


        radio2 => multiplicacion de radio por radio