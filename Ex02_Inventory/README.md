# Ex03: Inventory Management System

### Objetivo

Desarrollar un sistema orientado a objetos en Python para gestionar el inventario de una tienda, utilizando **diccionarios y sus métodos** clave: `.get()`, `.pop()`, `.items()`, `.update()`, etc.

---

## Especificaciones Técnicas

### Clase `InventoryManagement`

#### Atributos:

- `inventory`: Diccionario que almacena `{product: quantity}`.

#### Métodos requeridos:

1. `__init__(self)`
   Inicializa el diccionario `inventory` vacío

2. `add_product(self, product, quantity)`

   - Añade un nuevo producto o **actualiza** la cantidad si ya existe
   - Asegúrate de que la cantidad sea un número entero positivo

3. `delete_product(self, product)`

   - Elimina un producto del inventario si existe, usando `.pop()`
   - Si no existe, muestra un mensaje: `"Producto no encontrado para eliminar"`

4. `consult_product(self, product)`

   - Devuelve la cantidad usando `.get()`
   - Si no existe, devuelve: `"Producto no existe en el inventario"`

5. `mod_quantity(self, product, new_quantity)`

   - Cambia el valor del producto dado por una nueva cantidad
   - Si no existe, avisa al usuario

6. `find_product(self, text)`

   - Muestra productos que contengan la palabra o parte del texto introducido
   - Útil para búsquedas parciales

7. `view_inventory(self, sort=False)`

   - Imprime todos los productos y sus cantidades
   - Si `sort=True`, lo muestra en orden alfabético

---

## Ejecución obligatoria

1. Crear un objeto `tienda = InventoryManagement()`
2. Añadir productos:

   ```python
   tienda.add_product("Manzanas", 10)
   tienda.add_product("Peras", 5)
   tienda.add_product("Manzanas", 5)  # Total: 15
   ```

3. Consultar:

   ```python
   print("Consultar Manzanas:", tienda.consult_product("Manzanas"))
   ```

4. Mostrar:

   ```python
   tienda.view_inventory()
   ```

5. Eliminar "Peras" y volver a mostrar:

   ```python
   tienda.delete_product("Peras")
   print("Inventario después de eliminar Peras:")
   tienda.view_inventory()
   ```

---

## Extensión opcional: Menú interactivo

Crea un menú donde el usuario pueda:

- Añadir productos
- Consultar uno
- Eliminar uno
- Modificar cantidades
- Buscar por texto
- Mostrar inventario
- Salir del programa

---

## Resultado esperado mínimo

```bash
Consultar Manzanas: 15

--- Inventario ---
Manzanas: 15
Peras: 5
------------------

Inventario después de eliminar Peras:
--- Inventario ---
Manzanas: 15
------------------
```
