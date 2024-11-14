class Tiendas:
  def __init__(self,nombre):
    self.nombre = nombre
    self.inventario = set()

  def agregar_producto(self, codigo, nombre):
    self.inventario.append({"codigo" : codigo, "nombre": nombre})

  def buscar_producto(self, codigo):
    #busca un producto por codigo en el inventario
    return codigo in self.inventario

  def __str__(self):
    return f"Tienda: {self.nombre, Inventario: {list(self.inventario)}"
