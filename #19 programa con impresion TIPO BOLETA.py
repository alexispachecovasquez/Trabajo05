#20
velocidad=float(input("ingrese el valor de a velocidad en m/s:"))
tiempo=float(input("Ingrese el valor del tiempo en segundos:"))
distancia=velocidad*tiempo
e=(distancia>100)
print(" + # Boleta de Distancia  +")
print(" + #################### +")
print("#")
print(" + # velocidad:",velocidad)
print(" + # tiempo :",tiempo)
print(" + # distancia :",distancia)
print(" + #################### +")
print("tuvo un gran recorrido?:",e)