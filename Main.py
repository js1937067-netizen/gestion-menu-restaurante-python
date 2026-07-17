"""
Problema 2: Gestión de precios de un menú de restaurante
----------------------------------------------------------
Aplica una promoción del 15% de descuento a los productos de una
categoría objetivo cuyo precio base supere un umbral definido.
"""

# ---------------------------------------------------------
# 1. Matriz del menú: [Nombre del Producto, Categoría, Precio Base]
# ---------------------------------------------------------
menu = [
    ["Hamburguesa Clásica", "Plato Fuerte", 25000],
    ["Pizza Familiar",      "Plato Fuerte", 45000],
    ["Ensalada César",      "Entrada",      18000],
    ["Sopa del Día",        "Entrada",      12000],
    ["Limonada Natural",    "Bebida",       8000],
    ["Gaseosa",              "Bebida",       6000],
    ["Torta de Chocolate",  "Postre",       15000],
    ["Helado",               "Postre",       9000],
]

# ---------------------------------------------------------
# 2. Parámetros de la promoción
# ---------------------------------------------------------
CATEGORIA_OBJETIVO = "Plato Fuerte"
UMBRAL_PRECIO = 20000
DESCUENTO = 0.15  # 15%


# ---------------------------------------------------------
# 3. Módulo (función) para calcular el precio final
# ---------------------------------------------------------
def calcular_precio_final(producto, categoria_objetivo=CATEGORIA_OBJETIVO,
                           umbral=UMBRAL_PRECIO, descuento=DESCUENTO):
    """
    Calcula el precio final de un producto aplicando la promoción
    si cumple con la categoría objetivo y supera el umbral de precio.

    producto: lista [nombre, categoria, precio_base]
    Retorna: (precio_final, promocion_aplicada: bool)
    """
    nombre, categoria, precio_base = producto

    if categoria == categoria_objetivo and precio_base > umbral:
        precio_final = precio_base * (1 - descuento)
        promocion_aplicada = True
    else:
        precio_final = precio_base
        promocion_aplicada = False

    return precio_final, promocion_aplicada


# ---------------------------------------------------------
# 4. Salida: mostrar cada producto con su precio base y final
# ---------------------------------------------------------
def mostrar_menu(menu):
    print(f"{'Producto':<22}{'Categoría':<15}{'Precio Base':>14}{'Precio Final':>15}  Promoción")
    print("-" * 80)

    for producto in menu:
        nombre, categoria, precio_base = producto
        precio_final, promo = calcular_precio_final(producto)

        estado = "Sí (-15%)" if promo else "No"
        print(f"{nombre:<22}{categoria:<15}${precio_base:>12,.0f} ${precio_final:>13,.0f}  {estado}")


if __name__ == "__main__":
    mostrar_menu(menu)
