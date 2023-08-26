edad=int(input("Ingrese su edad: "))
status= None
if (edad > 18) and (edad <30):
    status = "Es un adulto"
else:
    status ="No entran en la categoria correcta" 
print (status)
