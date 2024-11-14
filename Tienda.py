class Tienda:
  def __init__(self,nombre):
    self.nombre = nombre
    self.inventario = set()

  def agregar_producto(self, codigo):
    self.inventario.add(codigo)

  def buscar_producto(self, codigo):
    #busca un producto por codigo en el inventario
    return codigo in self.inventario

  def __str__(self):
    return f"Tienda: {self.nombre, Inventario: {list(self.inventario)}"
