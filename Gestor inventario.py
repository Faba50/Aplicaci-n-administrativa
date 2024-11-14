from Tienda import Tiendas

def gestionar_inventario():
    tiendas = {
        "Tienda1": Tienda("Tienda1"),
        "Tienda2": Tienda("Tienda2"),
        "Tienda3": Tienda("Tienda3")
    }

    # Agregar productos iniciales
    tiendas["Tienda1"].agregar_producto("001", "Laptop")
    tiendas["Tienda1"].agregar_producto("002", "Smartphone")
    tiendas["Tienda2"].agregar_producto("003", "Tablet")
    tiendas["Tienda2"].agregar_producto("004", "Cámara")
    tiendas["Tienda3"].agregar_producto("005", "Monitor")
    tiendas["Tienda3"].agregar_producto("006", "Teclado")

    while True:
        # Menú iterativo
        print("\n--- Menú de la tienda ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Agregar producto
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")

            print("¿En qué tienda desea agregar el producto?")
            for nombre_tienda in tiendas:
                print(nombre_tienda)
            tienda_seleccionada = input()

            tienda = tiendas.get(tienda_seleccionada)
            if tienda:
                tienda.agregar_producto(codigo, nombre)
                print(f"Producto {nombre} (código {codigo}) agregado a {tienda.nombre}.")
            else:
                print("La tienda seleccionada no existe.")
        
        elif opcion == "2":
            # Buscar producto
            codigo = input("Por favor indique el código del producto que busca: ")

            print("¿En qué tienda desea buscar?")
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
        
        elif opcion == "3":
            # Salir del menú
            print("Gracias por usar el sistema de inventario. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Llamada al método gestionar_inventario para ejecutar el menú
gestionar_inventario()
