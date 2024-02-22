#1.Una tienda de autopartes necesita un programa para catalogar sus productos,crear la clase catalogo
# y producto, realizar un objeto dentro de un catalgo de productos el cual debe tener un metodo para agregar
# productos el cual debe tener un metodo para agregar productos y otra para mostrar toda la lista de productos.

class Producto():
    def __init__(self, Nombre, Cantidad, Costo_Uni):
        self.Nombre=Nombre
        self.Cantidad=Cantidad
        self.Costo_Uni=Costo_Uni
        self.Costo_total=Cantidad*Costo_Uni

    def __str__(self):
        return f"{self.Nombre}"

    def Descripcion(self):
        print(self.Nombre,":", sep="")
        print("·Costo Unitario:", self.Costo_Uni)
        print("·Cantidad:", self.Cantidad)
        print("·Costo Total:", self.Costo_total)

class catalogo:
    productos_list=None
    def __init__(self):
        self.productos_list=[]

    def añadir_producto(self):
        Nombre=input("Ingrese el nombre del producto: ")
        Cantidad=int(input("Ingrese la cantidad: "))
        Costo_Uni=int(input("Ingrese el costo unitario del producto: "))
        producto=Producto(Nombre, Cantidad, Costo_Uni)
        self.productos_list.append(producto)

    def getList(self):
        for contacto in self.productos_list:
            print(contacto)

lista_Productos=catalogo()

while True:
    msg=""" Bienvenidos, que desea hacer?
    1. Añadir producto
    2. Ver lista de produstos añadidos
    3. Salir
    """
    print(msg)
    op=int(input(" Ingrese su opcion: "))
    if op==1:
        lista_Productos.añadir_producto()
    elif op==2:
        lista_Productos.getList()
    elif op==3:
        print("Hasta luego!!!")
        break
