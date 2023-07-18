import xml.etree.ElementTree as ET

ruta = "10o B\operaciones.xml"

arbol = ET.parse(ruta)

raiz = arbol.getroot()

for operacion in raiz.findall("operacion"):
    tipoOperacion = operacion.find("tipo").text
    num1 = operacion.find("operando1").text
    num2 = operacion.find("operando2").text

    if tipoOperacion == "suma":
        resultado = int(num1) + int(num2)
        print("La suma es: ", resultado)
    elif tipoOperacion == "resta":
        resultado = int(num1) - int(num2)
        print("La resta es: ", resultado)
    elif tipoOperacion == "multiplicacion":
        resultado = int(num1) * int(num2)
        print("La multiplicacion es: ", resultado)
    elif tipoOperacion == "division":
        resultado = int(num1) / int(num2)
        print("La division es: ", resultado)
    else:
        print("Operacion no valida")
