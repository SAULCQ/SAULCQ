#4. crear un archivo nuevo y realizar una funcion que permita dividir 2 numeros, importar esta funcion
# ponerlo en un bucle while True , y al ser llamada la importacion ponerlo dentro de un try except 
# ejecutar la funcion hasta que realice correctamente la division luego de eso romper el bucle

import Division
while True:
    try: 
        Division.Dividir()
        break
    except Exception as e:
        print(e)
        continue


