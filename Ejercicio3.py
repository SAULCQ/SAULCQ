#Ejercicio 3
Ingresos=int(input("Registre los ingresos totales de su hogar: "))
Gasto1=int(input("ingrese la cantidad de gastos por comida: "))
Gasto2=int(input("ingrese la cantidad de gastos por movilidad: "))
Gasto3=int(input("ingrese la cantidad de gastos por alquiler de vivienda: "))
Gasto4=int(input("ingrese la cantidad de gastos por recibos de sirvicios (luz, agua, etc): "))
Gasto5=int(input("ingrese un gasto adiciinal que usted cree que debe considerar: "))
GastoTotal=Gasto1+Gasto2+Gasto3+Gasto4+Gasto5
Ahorro=Ingresos-GastoTotal
msg1=f"Los egresos totales de su hogar son {GastoTotal} soles y el ahorro es de {Ahorro} soles"
print(msg1)
