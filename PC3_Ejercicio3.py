#3. Del siguiente texto :
"""
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""
# realizar al menos 4 funciones de string 

Mensaje="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
Interfaz="""Opciones:
1. Todo en minuscula
2. Todo en Mayuscula
3. Primera letra en mayuscula
4. Primera letra de cada palabra en mayuscula
5. Salir"""
while True:
    print(Interfaz)
    opcion=int(input("Ingrese su opcion: "))
    if opcion==1:
        Mensaje=Mensaje.lower()
        print(Mensaje)
    elif opcion==2:
        Mensaje=Mensaje.upper()
        print(Mensaje)
    elif opcion==3:
        Mensaje=Mensaje.capitalize()
        print(Mensaje)
    elif opcion==4:
        Mensaje=Mensaje.title()
        print(Mensaje)
    elif opcion==5:
        print("Hasta Luego!!!!")
        break
    else:
        print("Escoger una opcion correcta!!!")

