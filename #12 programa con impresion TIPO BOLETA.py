#12
planeta=input("ingrese el nombre del planeta en que vive:")
p=int(input("ingrese el % de la contaminacion del planeta:"))
c=int(input("ingrese el % del planeta en su maxima vida:"))
vida=(c-p)
cuerpo_en_destruccion=(vida<49)
print("###################")
print("# vida del planeta #")
print("####################")
print("#")
print("# planeta",planeta)
print("# item:",p,"de contaminacion")
print("# item:",c,"de cuidados")
print("# vida:",vida)
print("#####################")
print("cuerpo_en_destruccion?",cuerpo_en_destruccion)
