#4
luchador=input("ingrese el nombre del luchador:")
peleas=int(input("ingrese el numero de peleas:"))
precio=int(input("ingrese el precio por pelea:"))
ganancia=(peleas*precio)
luchador_entreno = (ganancia>1000)
print(" + #################### +")
print(" + # lucha libre +")
print(" + #################### +")
print("#")
print(" + # luchador:",luchador)
print(" + # item :",peleas,"rondas")
print(" + # item :",precio," por lucha")
print(" + # ganancia:",ganancia)
print(" + #################### +")
print("luchador_entreno?:",luchador_entreno)