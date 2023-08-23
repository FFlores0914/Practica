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
    print ("4. Division")
    print ("5.Salir")
    opcion = input ("Seleccione una Opcion. ")

    if opcion == "5":
        print ("Hasta Luego")
        break

    num1=float(input("Ingrese un numero. "))
    num2=float(input("Ingrese un numero. "))

    if opcion=="1":
        print ("Resultado: ", suma(num1, num2))
    elif opcion=="2":
        print ("Resultado: ", resta(num1, num2))
    elif opcion=="3":
        print ("Resultado: ", multiplicacion(num1, num2))
    elif opcion=="4":
        print ("Resultado: ", division(num1, num2))
    else:
        print("Opcion Invalida.")