# Calculadora de tarifas de traslados - Versión 1

PRECIO_POR_KM = 1000.0

km_hasta_cliente = float(input("Km hasta el cliente: "))
km_con_cliente = float(input("Km de viaje con el cliente: "))

km_totales = km_hasta_cliente + km_con_cliente
total = km_totales * PRECIO_POR_KM

print(f"Total a cobrar: ${total:.2f}")