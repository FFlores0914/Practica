def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b !=0:
        return a / b
    else:
        return "No se puede dividir entre 0"
while True:
    print ("Opciones.")
    print ("1. Suma.")
    print ("2. resta.")
    print ("3. Multiplicacione.")
    print ("4. Division.")
    print ("5. Salir.")

    opcion = input ("Seleccione una Opcion.")

    if opcion == "5":
        print ("Hasta Luego.")
        break


