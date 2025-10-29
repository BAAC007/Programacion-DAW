nombre_persona = input("Ingrese su nombre por favor: ")

nombre_producto = input("Ingrese el nombre del producto: ")

precio_base = int(input("Ingrese el precio base del producto: "))

almacenamiento_gb = int(input("Ingrese el almacenamiento del producto: "))

peso_g = float(input("Ingrese el peso del producto: "))

pantalla_pulgada = float(input("Ingrese las pulgadas de pantalla del producto: "))

presupuesto_maximo = int(input("Ingrese el precio maximo del producto: "))

IVA = 0.21

total_iva = precio_base * IVA

precio_total = precio_base + total_iva

almacenamiento_mb = almacenamiento_gb * 1024

peso_kg = peso_g / 1000


precio_falso = bool(precio_total == presupuesto_max > excede_presupuesto)

precio = precio_base > presupuesto_maximo

comparacion = bool(pantalla_pulgada > 6 and peso_kg < 1)

almacenamiento = bool(almacenamiento_gb == 0.5 or almacenamiento_mb == 512)