import xml.etree.ElementTree as ET 

ruta = "10o B\clases.xml"

arbol = ET.parse(ruta)

raiz = arbol.getroot()

for clase in raiz.findall("clase"):
    identi = clase.find("identi").text
    nombre = clase.find("nombre").text
    profesor = clase.find("profesor").text
    punteo = clase.find("punteo").text
    creditos = clase.find("creditos").text

    print(f"id : {identi} - Clase: {nombre} - Profesor: {profesor} - Punteo: {punteo} - Creditos: {creditos}")
