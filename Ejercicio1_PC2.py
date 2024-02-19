#1. Crear un menu iterativo con las siguientes opciones 
#2. opcion 1 'Saludar' , pedir datos personales
#3. opcion 2 Realizar una operacion matematica pedir 2 numeros 
#4. opcion 3 Agregar a lista un diccionario que tenga (nombre ,edad ,correo,cursos). Los cursos sera a su vez una lista de diccionario que tendra las llaves de nombre de curso y listado de notas
#5. opcion 4 calcular el promedio de las notas y agregar las notas finales a una lista  
#6. opcion 5 mostrar listado de alumnos aprobados 
#7. opcion 6 mostrar listado de alumnos desaprobados
#8. opcion 7 Generar una funcion rango hasta un numero grande (10^10) con un step y agregar a una lista los numeros que cumplan la condicion de ser multiplo de 2 ,  5 y de 7.Finalmente mostrar el tamaño de esa lista.
#9. opcion 8 llamar a una funcion que devuelva el mayor de 2 numeros ingresados por teclado.
#10. opcion 9 Salir. 
usuarios=[]  

def saludar():
    Nombre=input("Escriba su nombre, por favor: ")
    msg=f"Hola {Nombre}, espero que te encuentres bien!!!"
    return(msg)

def Multiplicar():
    N1=int(input("Ingrese el primer numero: "))
    N2=int(input("Ingrese el segundo numero: "))
    Resultado=N1*N2
    msg=f"El producto de ambos numeros es {Resultado}"
    return(msg)

def Rango():
    A=int(input("Ingresa un numero grande: "))
    numeros=range(A)
    multiplos=[]

    for i in numeros:
        if numeros[i]%2==0 and numeros[i]%5==0 and numeros[i]%7==0:
            multiplos.append(numeros[i])
        else:
            continue
    msg=f"La cantidad de multiplos existentes es: {len(multiplos)}"
    return msg

def Mayor():
    N1=int(input("Ingrese el primer numero: "))
    N2=int(input("Ingrese el segundo numero: "))
    if N1>N2:
        msg=f"El numero mayor es {N1}"
    elif N2>N1:
        msg=f"El numero mayor es {N2}"
    return(msg)

def Agregar_usuario():
    name=input("ingrese su nombre: ")
    dni=input("ingrese su dni: ")
    correo=input("ingrese su correo: ")
    registro={}
    while True:
        curso=input("Ingrese el curso: ")
        nota1=int(input("Ingrese la primera nota: "))
        nota2=int(input("Ingrese la segunda nota: "))
        nota3=int(input("Ingrese la tercera nota: "))
        notas=[nota1,nota2,nota3]
        registro[curso]=notas
        flag=input("Desea continuar agregando cursos? (Si/No): ")
        if flag.upper()=="SI":
            continue
        elif flag.upper()=="NO":
            break
    datos={
        'Nombre':name,
        'DNI':dni,
        'Correo':correo,
        'Cursos':registro
        }
    usuarios.append(datos)

def Promedio():
    for i in usuarios:
        nombre=i["Nombre"]
        print(nombre)
        for curso, notas in i["Cursos"].items():
            promedio_curso = sum(notas) / len(notas)
            print(f"Promedio de notas en {curso}: {promedio_curso}")

while True:
    print("Bienvenido, ingrese la opción que desee")
    opciones="""        1. Saludar
        2. Multiplicar dos numeros
        3. Registrar datos
        4. Promedio de las notas
        5. Alumnos aprobados
        6. Alumnos desaprobados
        7. Multiplos de  2, 5 y 7
        8. Numero mayor
        9. Salir"""
    print(opciones)
    opc=int(input("Ingrese la opción que desea: "))
    if opc==1:
       print(saludar(),"\n") 

    elif opc==2:
        print(Multiplicar(),"\n")

    elif opc==3:
        Agregar_usuario()
        for i,item in enumerate(usuarios):
            print(i+1,".",item)

    elif opc==4:
        print(Promedio(),"\n")

    elif opc==7:
        print(Rango(),"\n")   

    elif opc==8:
        print(Mayor(),"\n")

    elif opc==9:
        print("HASTA LUEGO !!!")
        break

    else:
        print("Elija una opción correcta")