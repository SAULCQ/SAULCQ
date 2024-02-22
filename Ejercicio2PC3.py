#2. Realizar un programa que tenga una clase producto el cual solo tiene los atributos de nombre y codigo
# el codigo tiene la siguiente estructura PAIS-LOTE-AÑO ejemplo:PERU-00001-2024 crear un metodo que imprima el objeto de forma 
# literal (__str__) y que permita identificar el pais de origen y nro de lote

class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
    
    def __str__(self):
        pais, lote, año = self.codigo.split("-")
        return f"Producto: {self.nombre}, Origen: {pais}, Número de lote: {lote}"
    
producto1 = Producto("Gaseosa", "Chile-05541-2024")
print(producto1) 