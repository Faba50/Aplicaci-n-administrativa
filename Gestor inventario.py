from Tienda import Tiendas

def gestionar_inventario():
    tiendas = {
        "Tienda1": Tienda("Tienda1"),
        "Tienda2": Tienda("Tienda2"),
        "Tienda3": Tienda("Tienda3")
    }

    
    tiendas["Tienda1"].agregar_producto("001")
    tiendas["Tienda1"].agregar_producto("002")
    tiendas["Tienda2"].agregar_producto("003")
    tiendas["Tienda2"].agregar_producto("004")
    tiendas["Tienda3"].agregar_producto("005")
    tiendas["Tienda3"].agregar_producto("006")

    
    codigo = input("Por favor indique el código del producto que busca: ")

    
    print("¿En qué tienda desea buscar? ")
    for nombre in tiendas:
        print(nombre)
    nombre_tienda = input()

    
    tienda = tiendas.get(nombre_tienda)
    if tienda:
        if tienda.buscar_producto(codigo):
            print(f"El producto con código {codigo} está disponible en {tienda.nombre}.")
        else:
            print(f"El producto con código {codigo} no está disponible en {tienda.nombre}.")
    else:
        print("La tienda seleccionada no existe.")



gestionar_inventario()
