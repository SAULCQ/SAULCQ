#Ejercicio 2
import math
A=int(input("Ingrese el número del poligono con el que quiere trabajar 1.Triangulo 2.Cuadrado 3.Circulo : "))
if A==1:
    alturaT=int(input("Ingrese la altura del triangulo del triangulo: "))
    ladoT=int(input("Ingrese la longitud de los lados del tiangulo: "))
    areaT=ladoT*alturaT/2
    perimetroT=ladoT*3
    msg1=f"El area del triangulo que ingresaste es {areaT} metros cuadrados y el perimetro es {perimetroT} metros."
    print(msg1)
elif A==2:
    ladoC=int(input("Ingrese la longitud de los lados del cuadrado: "))
    areaC=pow(ladoC,2)
    perimetroC=ladoC*4
    msg2=f"El area del cuadrado que ingresaste es {areaC} metros cuadrados y el perimetro es {perimetroC} metros."
    print(msg2)
elif A==3:
    r=int(input("Ingrese el radio del circulo: "))
    PI=math.pi
    areaCir=PI*pow(r,2)
    perimetroCir=2*PI*r
    msg3=f"El area del circulo que ingresaste es {areaCir} metros cuadrados y el perimetro es {perimetroCir} metros."
    print(msg3)
else:
    msgError=f"El numero {A} que ingresaste no está permitido"
    print(msgError)




