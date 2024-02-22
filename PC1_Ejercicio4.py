# Ejercicio 4
Edad=input("Ustes es mayor de edad? (Si/No): ")
Ruc=input("Usted cuenta con RUC? (Si/No): ")
Nombre=input("Usted cuenta con un nombre comercial? (Si/No): ")
if Edad.upper()=="SI":
    if Ruc.upper()=="SI":
        if Nombre.upper()=="SI":
            print("Ustes es apto para abrir un comercio")
        
        else:
            print("Ustes NO es apto para abrir un negocio")
    else:
        print("Ustes NO es apto para abrir un negocio")    
else:
    print("Ustes NO es apto para abrir un negocio")
